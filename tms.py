from math import exp
from z3 import *

class Node:
    def __init__(self, label, probability):
        self.label = label
        self.probability = probability

class Constraint:
    def __init__(self, label, relation, nodes, probability):
        self.label = label
        self.relation = relation
        self.nodes = nodes
        self.probability = probability

def funWithNone(f, p1, p2):
    if p1 is None:
        return p2
    elif p2 is None:
        return p1
    else:
        return f(p1, p2)

class TMS_Base:
    def __init__(self):
        self.nodes = {}
        self.constraints = {}

    def node_by_label(self, label):
        if label in self.nodes:
            return label
        return self.create_node(label)

    def create_node(self, label, probability=None):
        if label in self.nodes:
            old = self.nodes[label]
            probability = funWithNone(max, probability, old.probability)
        self.nodes[label] = Node(label, probability)
        return label

    def justify_node(self, label, conclusion, premises, probability=None):
        return self.add_constraint(
            label,
            lambda xs: Implies(And(*xs[1:]), xs[0]),
            [conclusion] + premises,
            probability)

    def add_constraint(self, label, relation, nodes, probability=None):
        assert label not in self.constraints
        self.constraints[label] = Constraint(label, relation, nodes, probability)
        return label

    def enable_assumption(self, node, value=True, probability=None):
        key = "assumption "+node
        if key in self.constraints:
            self.retract_constraint(key)
        return self.add_constraint(
            key,
            lambda xs: xs[0] if value else Not(xs[0]),
            [node],
            probability)

    def retract_node(self, key):
        node = self.nodes.pop(key)
        for (k,constraint) in list(self.constraints.items()):
            if key in constraint.nodes:
                self.retract_constraint(k)

    def retract_constraint(self, key):
        del self.constraints[key]
    
    def maxsats(self):
        vars = self._create_vars()
        s = self._init_optimizer()
        self._add_constraints(s, vars)
        return self._find_models(s, vars)

    def maxsat(self):
        return self.maxsats()[0]

    def _create_vars(self):
        vars = {}
        for x in self.nodes.keys():
            vars[x] = Bool(x)
        return vars

    def _add_constraints(self, s, vars):
        def to_vars(xs):
            return [vars[x] for x in xs]
        def add_soft(x, p):
            if p < 0.5:
                self._add_clause(s, vars, Not(x), exp(-p))
            else:
                self._add_clause(s, vars, x, exp(-(1-p)))
        for (x,node) in self.nodes.items():
            if node.probability is not None:
                add_soft(vars[x], node.probability)
        for (x,constraint) in self.constraints.items():
            prop = constraint.relation(to_vars(constraint.nodes))
            if constraint.probability is not None:
                add_soft(prop, constraint.probability)
            else:
                self._add_clause(s, vars, prop)


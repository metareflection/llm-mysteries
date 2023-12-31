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

class TMS:
    def __init__(self):
        self.nodes = {}
        self.constraints = {}
        self.node_counter = 0
        self.constraint_counter = 0

    def node_by_label(self, label):
        for (x,node) in self.nodes.items():
            if node.label == label:
                return x
        return self.create_node(label, probability=0.0)

    def create_node(self, label, probability=None):
        key = self._node_key(label)
        self.nodes[key] = Node(label, probability)
        return key

    def justify_node(self, label, conclusion, premises, probability=None):
        return self.add_constraint(
            label,
            lambda xs: Implies(And(*xs[1:]), xs[0]),
            [conclusion] + premises,
            probability)

    def add_constraint(self, label, relation, nodes, probability=None):
        key = self._constraint_key(label)
        self.constraints[key] = Constraint(label, relation, nodes, probability)
        return key

    def enable_assumption(self, node, value=True, probability=None):
        return self.add_constraint(
            "assumption "+node,
            lambda xs: xs[0] if value else Not(xs[0]),
            [node],
            probability)

    def maxsat(self):
        vars = self._create_vars()
        s = Optimize()
        self._add_constraints(s, vars)
        assert s.check() == sat
        model = s.model()
        return self._model_by_label(model, vars)

    def _model_by_label(self, model, vars):
        m = {}
        for (x,node) in self.nodes.items():
            assert node.label not in m
            m[node.label] = model[vars[x]]
        return m

    def _create_vars(self):
        vars = {}
        for x in self.nodes.keys():
            vars[x] = Bool(x)
        return vars

    def _add_constraints(self, s, vars):
        def to_vars(xs):
            return list(map(lambda x: vars[x], xs))
        for (x,node) in self.nodes.items():
            if node.probability is not None:
                v = vars[x]
                s.add_soft(Not(v), exp(-node.probability))
        for (x,constraint) in self.constraints.items():
            prop = constraint.relation(to_vars(constraint.nodes))
            if constraint.probability is not None:
                s.add_soft(prop, exp(-constraint.probability))
            else:
                s.add(prop)

    def _node_key(self, label):
        key = "n"+str(self.node_counter)
        self.node_counter += 1
        return key

    def _constraint_key(self, label):
        key = "c"+str(self.constraint_counter)
        self.constraint_counter += 1
        return key

def ex1():
    tms = TMS()
    na = tms.create_node("a")
    nb = tms.create_node("b")
    nc = tms.create_node("c")
    nd = tms.create_node("d")
    ne = tms.create_node("e")
    nf = tms.create_node("f")
    ng = tms.create_node("g")
    tms.justify_node("j1", nf, [na, nb])
    tms.justify_node("j2", ne, [nb, nc])
    tms.justify_node("j3", ng, [na, ne])
    tms.justify_node("j4", ng, [nd, ne])
    tms.enable_assumption(na)
    tms.enable_assumption(nb)
    tms.enable_assumption(nc)
    tms.enable_assumption(nd)
    return tms.maxsat()

def ex2():
    tms = TMS()
    na = tms.create_node("a", probability=0.9)
    nb = tms.create_node("b", probability=0.9)
    nc = tms.create_node("c", probability=0.9)
    nd = tms.create_node("d")
    ne = tms.create_node("e")
    nf = tms.create_node("f")
    ng = tms.create_node("g")
    tms.justify_node("j1", nf, [na, nb])
    tms.justify_node("j2", ne, [nb, nc])
    tms.justify_node("j3", ng, [na, ne])
    tms.justify_node("j4", ng, [nd, ne])
    return tms.maxsat()

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

class TMS:
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
        vs = []
        def to_vars(xs):
            return [vars[x] for x in xs]
        def add_soft(x, p):
            vs.append(If(x, exp(-p), exp(-(1-p))))
        for (x,node) in self.nodes.items():
            if node.probability is not None:
                add_soft(vars[x], node.probability)
        for (x,constraint) in self.constraints.items():
            prop = constraint.relation(to_vars(constraint.nodes))
            if constraint.probability is not None:
                add_soft(prop, constraint.probability)
            else:
                s.add(prop)
        s.minimize(Sum(vs))

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

def ex3():
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
    r1 = tms.maxsat()
    tms.retract_node(ne)
    r2 = tms.maxsat()
    return (r1, r2)

def ex4():
  tms = TMS()
  na = tms.create_node("a", probability=0.9)
  model = tms.maxsat()
  assert model == {"a": True}
  return model

def ex5():
  tms = TMS()
  na = tms.create_node("a", probability=0.9)
  nb = tms.create_node("b", probability=0.4)
  nc = tms.create_node("c")
  tms.add_constraint("j1", lambda xs: Implies(And(xs[0], Not(xs[1])), xs[2]), [na, nb, nc], probability=0.9)
  model = tms.maxsat()
  assert model == {"a": True, "b": False, "c": True}
  return model

def ex6():
    tms = TMS()
    na = tms.create_node("a")
    nb = tms.create_node("b")
    nc = tms.create_node("c")
    tms.justify_node("j1", nc, [na, nb])
    tms.enable_assumption(na)
    tms.enable_assumption(nb)
    r1 = tms.maxsat()
    tms.enable_assumption(na, value=False)
    r2 = tms.maxsat()
    return (r1, r2)

if __name__ == '__main__':
    print(ex1())
    print(ex2())
    print(ex3())
    print(ex4())
    print(ex5())
    print(ex6())

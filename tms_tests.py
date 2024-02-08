from tms_z3 import TMS_Z3, TMS_Z3Symbolic
from tms_rc2 import TMS_RC2
from z3 import *

def ex1(TMS):
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

def ex2(TMS):
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

def ex3(TMS):
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

def ex4(TMS):
  tms = TMS()
  na = tms.create_node("a", probability=0.9)
  model = tms.maxsat()
  print(model)
  assert model == {"a": True}
  return model

def ex5(TMS):
  tms = TMS()
  na = tms.create_node("a", probability=0.9)
  nb = tms.create_node("b", probability=0.4)
  nc = tms.create_node("c")
  tms.add_constraint("j1", lambda xs: Implies(And(xs[0], Not(xs[1])), xs[2]), [na, nb, nc], probability=0.9)
  model = tms.maxsat()
  assert model == {"a": True, "b": False, "c": True}
  return model

def ex6(TMS):
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

def ex7(TMS):
    tms = TMS()
    na = tms.create_node("a")
    tms.add_constraint("a yes", lambda xs: xs[0], [na])
    tms.add_constraint("a no", lambda xs: Not(xs[0]), [na])
    r = tms.maxsat()
    assert r is None # unsatisfiable
    return r

def all_exs(TMS):
    print(ex1(TMS))
    print(ex2(TMS))
    print(ex3(TMS))
    print(ex4(TMS))
    print(ex5(TMS))
    print(ex6(TMS))
    print(ex7(TMS))

if __name__ == '__main__':
    all_exs(TMS_Z3)
    all_exs(TMS_RC2)
    print(ex1(TMS_Z3Symbolic))

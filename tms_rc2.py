from tms import TMS_Base
from z3 import *
from pysat.examples.rc2 import RC2
from pysat.formula import WCNF

def convert_to_cnf(formula, vars):
    cnf_tactic = Tactic('tseitin-cnf')
    cnf_formula = cnf_tactic(formula)
    assert len(cnf_formula) == 1
    return cnf_to_clauses(cnf_formula[0], vars)

def cnf_to_clauses(cs, vars):
    clauses = []
    for c in cs:
        if is_or(c):
            clauses.append([get_literal(x, vars) for x in c.children()])
        else:
            clauses.append([get_literal(c, vars)])
    return clauses

def get_literal(x, vars):
    if is_not(x):
        return -get_pos(x.children()[0], vars)
    else:
        return get_pos(x, vars)

def get_pos(x, vars):
    kx = str(x)
    if kx not in vars:
        vars[kx] = x
    return list(vars.values()).index(x)+1

def Xors(*xs):
    clauses = []
    for i in range(len(xs)):
        cs = [Not(x) for x in xs]
        cs[i] = xs[i]
        clauses.append(And(*cs))
    return Or(*clauses)

class TMS_RC2(TMS_Base):
    def __init__(self):
        super().__init__()

    def _init_optimizer(self):
        return WCNF()

    def _find_models(self, s, vars):
        with RC2(s) as rc2:
            c = None
            rs = []
            for model in rc2.enumerate():
                if c is None:
                    c = rc2.cost
                if c == rc2.cost:
                    rs.append(self._model_by_label(model))
                else:
                    return rs
            return rs

    def _model_by_label(self, model):
        m = {}
        for ((x,node),v) in zip(self.nodes.items(), model):
            assert node.label not in m
            m[node.label] = v > 0
        return m

    def _add_clause(self, s, vars, formula, weight=None):
        cnf = convert_to_cnf(formula, vars)
        for c in cnf:
            s.append(c, weight)

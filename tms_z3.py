from tms import TMS_Base
from z3 import *

def Xors(*xs):
    return Sum([If(x, 1, 0) for x in xs]) == 1

class TMS_Z3Base(TMS_Base):
    def __init__(self):
        super().__init__()
    
    def _find_models(self, s, vars):
        r = s.check()
        if r == sat:
            model = s.model()
            # TODO: find _all_ models with best cost
            return [self._model_by_label(model, vars)]
        else:
            assert r == unsat or r == unknown
            return []

    def _model_by_label(self, model, vars):
        m = {}
        for (x,node) in self.nodes.items():
            assert node.label not in m
            m[node.label] = model[vars[x]]
        return m

class TMS_Z3Symbolic(TMS_Z3Base):
    def __init__(self):
        super().__init__()

    def _init_optimizer(self):
        return Solver()

    def _add_clause(self, id, s, vars, formula, weight=None):
        assert(weight is None)
        s.add(formula)
    
class TMS_Z3(TMS_Z3Base):
    def __init__(self):
        super().__init__()

    def _init_optimizer(self):
        return Optimize()

    def _add_clause(self, id, s, vars, formula, weight=None):
        if weight is not None:
            s.add_soft(formula, weight)
        else:
            s.add(formula)
            

class TMS_Z3X(TMS_Z3):
    def __init__(self):
        super().__init__()
        self.soft_clauses = {}
        self.s = None

    def _init_optimizer(self):
        self.s = super()._init_optimizer()
        return self.s

    def _add_clause(self, id, s, vars, formula, weight=None):
        super()._add_clause(id, s, vars, formula, weight)
        if weight is not None:
            self.soft_clauses[id] = formula

    def belief_changes(self):
        m = self.s.model()
        return [id
                for (id,clause) in self.soft_clauses.items()
                if not m.evaluate(clause)]

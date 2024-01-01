from tms import TMS_Base
from z3 import *

class TMS_Z3(TMS_Base):
    def __init__(self):
        super().__init__()

    def _init_optimizer(self):
        return Optimize()

    def _find_models(self, s, vars):
        assert s.check() == sat
        model = s.model()
        # TODO: find _all_ models with best cost
        return [self._model_by_label(model, vars)]

    def _model_by_label(self, model, vars):
        m = {}
        for (x,node) in self.nodes.items():
            assert node.label not in m
            m[node.label] = model[vars[x]]
        return m

    def _add_clause(self, s, vars, formula, weight=None):
        if weight is not None:
            s.add_soft(formula, weight)
        else:
            s.add(formula)
            

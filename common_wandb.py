import wandb

class WandbWrapper:
    def __init__(self, run):
        self.run = run
        self.sum = 0

def log_eval(w, b, extras={}):
    if w:
        inc = 1 if b else 0
        w.sum += inc
        w.run.log({"eval": inc, "sum": w.sum} | extras)
    
def init(project):
    w = WandbWrapper(wandb.init(project=f"llm-mysteries_{project}"))
    return w



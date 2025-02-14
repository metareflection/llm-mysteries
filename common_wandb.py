import wandb

class WandbWrapper:
    def __init__(self, run):
        self.run = run
        self.sum = 0
        self.avg = 0.0
        self.n = 0

def log_eval(w, b, extras={}):
    if w:
        inc = 1 if b else 0
        w.sum += inc
        w.n += 1
        w.avg = (w.avg*(w.n-1)*1.0 + inc*1.0) / w.n
        w.run.log({"eval": inc, "sum": w.sum, "avg": w.avg} | extras)
    
def init(project):
    w = WandbWrapper(wandb.init(project=f"llm-mysteries_{project}"))
    return w



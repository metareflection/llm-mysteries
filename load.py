from markers import preambule, postambule
from datasets import load_dataset
import common_wandb

task_json = 'BIG-bench/bigbench/benchmark_tasks/minute_mysteries_qa/multiplechoice/task.json'
#task_json = 'tiny.json'

dataset = load_dataset('json', data_files=task_json, field='examples')

def tagline(x):
    return x['comment']

def story_text(x):
    return x['input']

def suspects(x):
    return [k for k,v in x['target_scores'].items() if v is not None]

def culprit(x):
    return [k for k,v in x['target_scores'].items() if v==1][0]

def generateCase(generate, extract, x, run=None):
    print(f"## {x['comment']}")
    r = generate(f"<s>[INST]{preambule}\n{x['input']}\n{postambule}[/INST]\n")
    s = extract(r, suspects(x))
    print(f"The culprit is {s}.")
    print(f"\nIn fact, it is {culprit(x)}.")
    x['eval'] = s == culprit(x)
    common_wandb.log_eval(run, x['eval'])
    return x
    
def generateAll(generate, extract):
    run = common_wandb.init(project="main")
    results = dataset.map(lambda x: generateCase(generate, extract, x, run))
    solved = len(list(1 for e in results['train']['eval'] if e==1))
    total = results.num_rows['train']
    print(f"Solved {solved} out of {total}.")

def generate1(generate, extract, i=0):
    generateCase(generate, extract, dataset['train'][i])

from markers import preambule, postambule
from datasets import load_dataset

task_json = 'BIG-bench/bigbench/benchmark_tasks/minute_mysteries_qa/multiplechoice/task.json'
#task_json = 'tiny.json'

dataset = load_dataset('json', data_files=task_json, field='examples')

def suspects(x):
    return [k for k,v in x['target_scores'].items() if v is not None]

def culprit(x):
    return [k for k,v in x['target_scores'].items() if v==1][0]

def generateCase(generate, extract, x):
    print(f"## {x['comment']}")
    r = generate(f"{preambule}\n{x['input']}\n{postambule}")
    s = extract(r, suspects(x))
    print(f"The culprit is {s}.")
    print(f"\nIn fact, it is {culprit(x)}.")
    x['eval'] = s == culprit(x)
    return x
    
def generateAll(generate, extract):
    results = dataset.map(lambda x: generateCase(generate, extract, x))
    solved = len(list(1 for e in results['train']['eval'] if e==1))
    total = results.num_rows['train']
    print(f"Solved {solved} out of {total}.")

from datasets import load_dataset

task_json = 'BIG-bench/bigbench/benchmark_tasks/minute_mysteries_qa/multiplechoice/task.json'

dataset = load_dataset('json', data_files=task_json, field='examples')

def suspects(x):
    return [k for k,v in x['target_scores'].items() if v is not None]

def culprit(x):
    return [k for k,v in x['target_scores'].items() if v==1][0]

def generateCase(generate, x):
    print(f"## {x['comment']}")
    r = generate(f"Who is the culprit?\n{x['input']}\nWho is the culprit?")
    print(f"\nIn fact, it was {culprit(x)}.")

def generateAll(generate):
    dataset.map(lambda x: generateCase(generate, x))

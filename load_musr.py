from markers import preambule, postambule
from datasets import load_dataset

task_json = 'MuSR/datasets/murder_mystery.json'

dataset = load_dataset('json', data_files=task_json)

def tagline(x):
    return 'STORY'

def story_text(x):
    return x['context']

def suspects(x):
    return x['questions'][0]['choices']

def culprit(x):
    return suspects(x)[x['questions'][0]['answer']]

def generateCase(generate, extract, x):
    print(f"## STORY")
    r = generate(f"{preambule}\n{x['context']}\n{postambule}")
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

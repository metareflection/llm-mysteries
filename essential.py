import outlines.text.generate.sample as sample
import outlines.text.generate as generate
import outlines.models as models
import torch
from transformers import BitsAndBytesConfig
from datasets import load_dataset

task_json = 'BIG-bench/bigbench/benchmark_tasks/evaluating_information_essentiality/task.json'

dataset = load_dataset('json', data_files=task_json, field='examples')

use_gpt = False
use_expansion = False
#base_model_name = "mistralai/Mistral-7B-v0.1"
base_model_name = "mistralai/Mixtral-8x7B-v0.1"
base_model_name = "mistralai/Mixtral-8x7B-Instruct-v0.1"
#base_model_name = "meta-llama/Llama-2-13b-hf"
#base_model_name = "meta-llama/Llama-2-70b-hf"

bnb_config = BitsAndBytesConfig(
    load_in_4bit=True,
    bnb_4bit_quant_type="nf4",
    bnb_4bit_compute_dtype=torch.float16,
)

def find_answer(r, choices):
    print(r)
    #answer = r[0]
    c = r
    while ')' in c:
        i = c.index(')')
        answer = c[i-1]
        if answer in choices:
            return answer
        c = c[i+1:]
    print('warning: non-conforming answer')
    return None

if use_gpt:
    from gpt import ask

    def gen_greedy(prompt, choices):
        r = ask(prompt, 'gpt-4-1106-preview')#, max_tokens=1)
        return find_answer(r, choices)
else:
    model = models.transformers(
    base_model_name,
    device="auto",
    model_kwargs={
        "quantization_config": bnb_config,
        #"device_map":"auto",
        "trust_remote_code": True,
        "use_auth_token": True,
    },
    )

    if use_expansion:
        def gen_greedy(prompt, choices):
            r = generate.continuation(model)(prompt)
            return find_answer(r, choices)
    else:
        def gen_greedy(prompt, choices):
            #unconstrained_answer = generate.continuation(model, max_tokens=3, sampler=sample.greedy)(prompt)
            #print('Unconstrained answer:', unconstrained_answer)
            return generate.choice(model, choices, sampler=sample.greedy)(prompt)

choices_dict = {
    "A": "Statement 1 alone is sufficient while statement 2 alone is insufficient",
    "B": "Statement 2 alone is sufficient while statement 1 alone is insufficient",
    "C": "Either statement 1 or statement 2 is sufficient",
    "D": "Statement 1 and statement 2 taken together are sufficient",
    "E": "Neither statement 1 nor statement 2 nor statements 1 and 2 taken together is sufficient",
    "F": "The question can be answered without either statement"
}


reverse_choices_dict = dict([(v,k) for k,v in choices_dict.items()])

def question_choices(x):
    r = dict([(reverse_choices_dict[k],k) for k,v in x['target_scores'].items() if v is not None])
    return dict([(k,v) for k,v in choices_dict.items() if k in r])

def answer(x):
    y = [k for k,v in x['target_scores'].items() if v==1][0]
    return reverse_choices_dict[y]
    
def process1(x):
    cur_choices_dict = question_choices(x)
    prompt = x['input']
    prompt += "\n\n"
    prompt += f"The options are one of {', '.join(['('+o+')' for o in cur_choices_dict.keys()])} as follows."
    prompt += "\n"
    prompt += '\n'.join([f"({k}). {v}." for k,v in cur_choices_dict.items()])
    prompt += "\n"
    prompt += f"The correct option is ("
    print(prompt)
    print('')
    correct_answer = answer(x)
    print('Correct answer:', correct_answer)
    given_answer = gen_greedy(prompt, cur_choices_dict.keys())
    print('Given answer:', given_answer)
    x['eval'] = given_answer == correct_answer
    print('')
    print('')
    return x

def processAll():
    results = dataset.map(process1)
    solved = len(list(1 for e in results['train']['eval'] if e==1))
    total = results.num_rows['train']
    print(f"Solved {solved} out of {total}.")

if __name__ == '__main__':
    processAll()

import outlines.text.generate.sample as sample
import outlines.text.generate as generate
import outlines.models as models
import torch
from transformers import BitsAndBytesConfig
from datasets import load_dataset

task_json = 'BIG-bench/bigbench/benchmark_tasks/evaluating_information_essentiality/task.json'

dataset = load_dataset('json', data_files=task_json, field='examples')

base_model_name = "meta-llama/Llama-2-13b-chat-hf"
#base_model_name = "meta-llama/Llama-2-70b-chat-hf"

bnb_config = BitsAndBytesConfig(
    load_in_4bit=True,
    bnb_4bit_quant_type="nf4",
    bnb_4bit_compute_dtype=torch.float16,
)

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

def gen_greedy(prompt, choices):
    return generate.choice(model, choices, sampler=sample.greedy)(prompt)

choices_dict = {
    "One": "Statement 1 alone is sufficient while statement 2 alone is insufficient",
    "Two": "Statement 2 alone is sufficient while statement 1 alone is insufficient",
    "Either": "Either statement 1 or statement 2 is sufficient",
    "Together": "Statement 1 and statement 2 taken together are sufficient",
    "Neither": "Neither statement 1 nor statement 2 nor statements 1 and 2 taken together is sufficient",
    "Already": "The question can be answered without either statement"
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
    prompt += '\n'.join([f"{k}: {v}." for k,v in cur_choices_dict.items()])
    prompt += "\n"
    prompt += f"Answer with exactly one of these words: {', '.join(cur_choices_dict.keys())}."
    prompt += "\n"
    print(prompt)
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

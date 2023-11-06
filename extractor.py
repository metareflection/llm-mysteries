from markers import postambule
import outlines.text.generate.sample as sample
import outlines.text.generate as generate
import outlines.models as models
import torch

#base_model_name = "mistralai/Mistral-7B-v0.1"
#base_model_name = "meta-llama/Llama-2-70b-hf" # takes forever!
#base_model_name = "meta-llama/Llama-2-13b-hf"
base_model_name = "meta-llama/Llama-2-13b-chat-hf"
model = models.transformers(base_model_name, device="cuda")

def extract(r, choices):
    i = r.index(postambule)
    prompt = r[i+len(postambule):]
    print(prompt)
    print("The suspects are "+",".join(choices))
    prompt += "\nSo as explained, the culprit is"
    return gen(prompt, choices)

def gen(prompt, choices):
    choices_repr = [repr(c) for c in choices]
    choices_repr_joined = ', '.join(choices_repr)
    print(f'gen({repr(prompt)}, [{choices_repr_joined}])')
    r = gen_greedy(prompt, choices)
    print(r)
    return r

def gen_greedy(prompt, choices):
    return generate.choice(model, choices, sampler=sample.greedy)(prompt)

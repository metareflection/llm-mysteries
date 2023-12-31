import outlines.text.generate.sample as sample
import outlines.text.generate as generate
import outlines.models as models
import torch
from transformers import BitsAndBytesConfig

#base_model_name = "mistralai/Mistral-7B-v0.1"
#base_model_name = "meta-llama/Llama-2-70b-hf"
#base_model_name = "meta-llama/Llama-2-13b-hf"
#base_model_name = "meta-llama/Llama-2-13b-chat-hf"
#base_model_name = "meta-llama/Llama-2-70b-chat-hf"
base_model_name = "mistralai/Mixtral-8x7B-Instruct-v0.1"

#model = models.transformers(base_model_name, device="cuda")
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

def extract(r, choices):
    i = r.index("[/INST]")
    prompt = r[i+len("[/INST]"):]
    prompt = f"<s>[INST]Who is the culprit based on this: {prompt}. Answer exactly one of {', '.join(choices)}.[/INST]"
    print(prompt)
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

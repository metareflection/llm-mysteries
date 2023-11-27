from markers import postambule
import outlines.text.generate.sample as sample
import outlines.text.generate as generate
import outlines.models as models
import torch
from transformers import BitsAndBytesConfig

#base_model_name = "mistralai/Mistral-7B-v0.1"
#base_model_name = "meta-llama/Llama-2-70b-hf" # takes forever!
#base_model_name = "meta-llama/Llama-2-13b-hf"
base_model_name = "meta-llama/Llama-2-13b-chat-hf"
#base_model_name = "meta-llama/Llama-2-70b-chat-hf"

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

# r is a parameter representing the result of the llm.generate() call in generateCase() in load.py
# so, r will return text representing the LLM output --> the prompt was originally preamble + story + postamble,
# so I think the LLM returns the original prompt before its output text
def extract(r, choices):
   i = r.index(postambule)
   prompt = r[i+len(postambule):]
   print(prompt) # filter out the prompt and only keep the actual output of the LLM (still naming the output prompt since it will be another prompt soon)
   print("The suspects are "+",".join(choices))

   # Here, we make another call to the LLM, to identify who the suspect is based on the reasoning it just outputted from the original call.
   prompt += "\nSo as explained, the culprit is"
   return gen(prompt, choices) # Thus, extract queries the LLM to find what character the LLM think is the guilty suspect



# this is query logic to the LLM, using the prompt from extract() and the list of suspects
def gen(prompt, choices):
   choices_repr = [repr(c) for c in choices]
   choices_repr_joined = ', '.join(choices_repr)
   print(f'gen({repr(prompt)}, [{choices_repr_joined}])') # just printing for our own reference what has been inputted to the LLM thus far
   r = gen_greedy(prompt, choices)
   print(r)
   return r

def gen_greedy(prompt, choices):
   # this is from outlines library, look into how this works, but probably just gets the highest logit from the LLM
   return generate.choice(model, choices, sampler=sample.greedy)(prompt)
from markers import postambule
import outlines.text.generate as generate
import outlines.models as models

#base_model_name = "mistralai/Mistral-7B-v0.1"
#base_model_name = "meta-llama/Llama-2-70b-hf" # takes forever!
base_model_name = "meta-llama/Llama-2-13b-hf"
model = models.transformers(base_model_name)

def extract(r, choices):
    i = r.index(postambule)
    prompt = r[i+len(postambule):]
    print(prompt)
    print("The suspects are "+",".join(choices))
    prompt += "\nThe culprit is"
    return generate.choice(model, choices)(prompt)

from markers import postambule
import outlines.text.generate as generate
import outlines.models as models

base_model_name = "mistralai/Mistral-7B-v0.1"
model = models.transformers(base_model_name)

def extract(r, choices):
    i = r.index(postambule)
    prompt = r[i+len(postambule):]
    return generate.choice(model, choices)(prompt)

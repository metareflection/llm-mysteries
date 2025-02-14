import os
from openai import AsyncOpenAI
import outlines
from outlines import models
from outlines.models.openai import OpenAIConfig
from outlines.samplers import greedy

client = AsyncOpenAI(
    api_key="ollama",
    base_url="http://localhost:11434/v1"
)
config = OpenAIConfig("qwen2.5")
model = models.openai(client, config)

def extract(r, choices):
    prompt = r
    prompt = f"Who is the culprit based on this: {prompt}. Answer exactly one of {', '.join(choices)}."
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
    return outlines.generate.choice(model, choices#, sampler=greedy()
                                    )(prompt)

if __name__ == '__main__':
    print(gen('What is more yellow, Vanilla or Chocolate?', ['Vanilla', 'Chocolate']))

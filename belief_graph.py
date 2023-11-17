from extractor import model, base_model_name
from sequence_probabilities import make_greedy_tracker
from outlines.text.generate.regex import choice
from transformers import AutoTokenizer
from math import exp
from load import dataset, suspects, culprit, tagline, story_text
import mystery

tokenizer = AutoTokenizer.from_pretrained(base_model_name, trust_remote_code=True)
tokenizer.pad_token = tokenizer.eos_token

bool_choices = ['True', 'False']

mask_token_ids = [tokenizer.encode(w, add_special_tokens=False)[-1] for w in bool_choices]

belief_generator = make_greedy_tracker(
    choice(model, bool_choices, max_tokens=50))

def belief_probability(prompt):
    question = prompt[0:prompt.index('?')+1]
    print(question)
    val = belief_generator(prompt)
    confidence = exp(belief_generator.sequence_log_prob)
    print(f"{val} ({confidence})")
    return (val, confidence)

def create_prompt(story, id, neg, what=None):
    postfix = ': True or False?'
    if what is None:
        prompt = f"{id} is{' not' if neg else ''} guilty"
    else:
        prompt = f"{id} has{' no' if neg else ''} mean"
    question = prompt + postfix
    return question + '\n' + story + '\n' + question

def create_story_lines(story, suspect_list):
    lines = []
    for suspect in suspect_list:
        for what in [None] + mystery.whats:
            for neg in [True, False]:
                (val, confidence) = belief_probability(create_prompt(story, suspect, neg, what))
                lines.append((suspect, what, val if not neg else not val, confidence))
    return lines

def solve(story, suspect_list):
    return mystery.solve(create_story_lines(story, suspect_list))

def processCase(x):
    print(f"## {tagline(x)}")
    found_culprit = solve(story_text(x), suspects(x))
    print(f"The culprit is {found_culprit}.")
    print(f"In fact, it is {culprit(x)}.")
    x['eval'] = found_culprit == culprit(x)
    return x

def processAll():
    results = dataset.map(processCase)
    solved = len(list(1 for e in results['train']['eval'] if e==1))
    total = results.num_rows['train']
    print(f"Solved {solved} out of {total}.")

if __name__ == '__main__':
    processAll()

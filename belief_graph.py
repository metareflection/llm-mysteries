from extractor import model, base_model_name
from sequence_probabilities import make_greedy_tracker
from outlines.text.generate.regex import choice
from transformers import AutoTokenizer
from math import exp
from load import dataset, suspects, culprit, tagline, story_text
import mystery
import spacy

tokenizer = AutoTokenizer.from_pretrained(base_model_name, trust_remote_code=True)
tokenizer.pad_token = tokenizer.eos_token

nlp = spacy.load('en_core_web_sm')

bool_choices = ['True', 'False']

mask_token_ids = [tokenizer.encode(w)[-1] for w in bool_choices]
mask_token_ids = [5574, 8824] # set it manually by inspection...

belief_generator = make_greedy_tracker(
    choice(model, bool_choices, max_tokens=50),
    mask_token_ids
)

def belief_probability(prompt):
    question = prompt[0:prompt.index('?')+1]
    print(question)
    belief_generator.sequence_log_prob = 0.0
    val = belief_generator(prompt)
    val = True if val=='True' else False
    confidence = exp(belief_generator.sequence_log_prob)
    print(f"{val} ({confidence})")
    return (val, confidence)

def create_prompt(sentence, id, neg, what=None):
    postfix = ': True or False?'
    if what is None:
        prompt = f"{id} is{' not' if neg else ''} guilty"
    else:
        prompt = f"{id} has{' no' if neg else ''} {what}"
    question = prompt + postfix

    with open("prompts.txt", "a") as f:
        f.write("=====BEGIN PROMPT======\n")
        f.write(question + '\n' + sentence + '\n' + question + "\n")
        f.write("======END PROMPT=====\n")

    return question + '\n' + sentence + '\n' + question

def create_story_lines(story, suspect_list):
    lines = []

    # sentences = story.split(".") 
    # Using NLP instead of a trivial .split(".") to split sentences
    doc = nlp(story)
    sentences = [sent.text.strip() for sent in doc.sents]

    for sentence in sentences:
        for suspect in suspect_list:
            for what in [None] + mystery.whats:
                #for neg in [True, False]:
                (val, confidence) = belief_probability(create_prompt(sentence, suspect, False, what))
                lines.append((suspect, what, val, confidence))
                lines.append((suspect, what, not val, 1.0-confidence))
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

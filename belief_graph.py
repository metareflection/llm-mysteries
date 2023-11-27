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

mask_token_ids = [tokenizer.encode(w)[-1] for w in bool_choices]
mask_token_ids = [5574, 8824] # set it manually by inspection... --> token_ids for True and False

# create a new custom text generator that tracks cumulative log probabilities (beliefs) for each generated sequence and focuses on the True & False tokens
belief_generator = make_greedy_tracker(
   choice(model, bool_choices, max_tokens=50),
   mask_token_ids
)


# queries the LLM using the prompt parameter as input and returns the output along with the calculated confidence (cumulative log probability)
def belief_probability(prompt):
   question = prompt[0:prompt.index('?')+1]
   print(question)
   belief_generator.sequence_log_prob = 0.0 # resets the cumulative log probability to be 0 (to represent the start of a new belief)
   val = belief_generator(prompt) # the RHS runs the __call__ method of the generator, so queries LLM using greedy strategy
   val = True if val=='True' else False
   confidence = exp(belief_generator.sequence_log_prob) # calculates confidence by doing e ^ (cumulative_log_probability)
   print(f"{val} ({confidence})")
   return (val, confidence)

# for what nodes: creates a prompt in the form of 'Character X has motive: True or False', 'Character Y has no mean: True or False'
# if no what node, asks the LLM for the final verdict on the suspect on whether or not they're guilty
def create_prompt(story, id, neg, what=None):
   postfix = ': True or False?'
   if what is None:
       prompt = f"{id} is{' not' if neg else ''} guilty"
   else:
       prompt = f"{id} has{' no' if neg else ''} {what}"
   question = prompt + postfix
   return question + '\n' + story + '\n' + question

# returns a list of all of the LLM's beliefs for each what node for each suspect 
def create_story_lines(story, suspect_list):
   lines = []
   # for each suspect
   for suspect in suspect_list:
       # for each what node
       for what in [None] + mystery.whats:
            # create a prompt for that what node and then ask the LLM to answer True or False (and get the belief of it)
           (val, confidence) = belief_probability(create_prompt(story, suspect, False, what))

           # store the belief and its inverse (for self consistency?) Is this negation? I don't think so since negation nodes were implemented
           # some other way. TODO: look into this further as to why we append the inverse.
           lines.append((suspect, what, val, confidence))
           lines.append((suspect, what, not val, 1.0-confidence))
   return lines

# solves the given mystery using the mystery.solve() function --> LOOK INTO THIS LATER
def solve(story, suspect_list):
   # parameter for mystery.solve() is return value of create_story_lines(), which is a list of all of the LLM's beliefs (beliefs on each what node for each suspect)
   return mystery.solve(create_story_lines(story, suspect_list))

# process a given mystery as such:
def processCase(x):
   print(f"## {tagline(x)}") # print the title of the mystery
   found_culprit = solve(story_text(x), suspects(x)) # get the actual text of the mystery and the suspect list, and pass into solve() function defined above
   print(f"The culprit is {found_culprit}.")
   print(f"In fact, it is {culprit(x)}.")
   x['eval'] = found_culprit == culprit(x) # in 'eval' column, store 0/1 for correctly identifying the culprit
   return x

# this function is similar to the generateAll() in load.py --> probably edited to use the belief graph approach while load.py
# was for just vanilla calls to the LLM
def processAll():
    # the processCase function gets applied to each row in the mysteries dataset, and we count how many got solved
   results = dataset.map(processCase)
   solved = len(list(1 for e in results['train']['eval'] if e==1))
   total = results.num_rows['train']
   print(f"Solved {solved} out of {total}.")

if __name__ == '__main__':
   processAll()

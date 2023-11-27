# this file contains the code for loading the 5 minute mysteries dataset, hence the name load --> don't get this confused with loading an LLM!
from markers import preambule, postambule
from datasets import load_dataset

task_json = 'BIG-bench/bigbench/benchmark_tasks/minute_mysteries_qa/multiplechoice/task.json'
#task_json = 'tiny.json'

# the examples field is what contains all of the actual examples in the dataset, so now we can treat the dataset we have as
# a table with the columns as 'input', 'target scores', and 'comment'
dataset = load_dataset('json', data_files=task_json, field='examples')

# the 'comment' column represents the name of each mystery
def tagline(x):
   return x['comment']

# the 'input' column represents the actual text of the story
def story_text(x):
   return x['input']

# each entry in the 'target scores' column is a dictionary that maps suspect names in string format to integers that are 0 or 1
# each dictionary has 4 suspect names, and of those 4, 1 of them is marked with a 1 (to represent the true answer for the culprit),
# while the other 3 have 0s to represent not guilty
def suspects(x):
   # for each suspect (key) and their corresponding mark as 0 or 1 (value), if the suspect has a defined value, then we can consider them as a
   # valid suspect and can add them to a list of suspects in the entire story.
   return [k for k,v in x['target_scores'].items() if v is not None]

# again, noticing the same 0/1 format as noted above, this function simply returns the suspect who has a value of 1 (the person actually guilty)
def culprit(x):
   return [k for k,v in x['target_scores'].items() if v==1][0]

def generateCase(generate, extract, x):
   print(f"## {x['comment']}")
   r = generate(f"{preambule}\n{x['input']}\n{postambule}") # call to the LLM
   s = extract(r, suspects(x)) # looks like extract returns the suspect that the model thinks is guilty
   print(f"The culprit is {s}.")
   print(f"\nIn fact, it is {culprit(x)}.")
   x['eval'] = s == culprit(x) # if the LLM guessed the suspect correctly, then represent the entry with a 1, otherwise 0 --> stored in 'eval' colun
   return x
  
def generateAll(generate, extract):
   # for each entry (mystery), call generateCase (aka solve and see if you get correct answer), with the 'eval' column now holding a 1 or 0 represent correct/incorrect
   results = dataset.map(lambda x: generateCase(generate, extract, x))
   
   # count how many mysteries were solved correctly
   solved = len(list(1 for e in results['train']['eval'] if e==1))
   total = results.num_rows['train']
   print(f"Solved {solved} out of {total}.")
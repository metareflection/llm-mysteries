# this is the original vanilla approach used to solve the mysteries with no additional techniques
import load
import llm
from extractor import extract

# solve each mystery case, passing in the LLM generate function and the extract function to get the answer to the guilty suspect from the LLM
load.generateAll(llm.generate, extract)

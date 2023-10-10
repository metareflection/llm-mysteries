import load
import llm
from extractor import extract

load.generateAll(llm.generate, extract)

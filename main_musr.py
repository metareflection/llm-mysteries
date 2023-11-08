import load_musr as load
import llm
from extractor import extract

load.generateAll(llm.generate, extract)

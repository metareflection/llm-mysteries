import load
import gpt
from extractor import extract

load.generateAll(gpt.generate, extract)

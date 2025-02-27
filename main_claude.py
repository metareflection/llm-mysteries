import load
import claude
from extractor import extract

load.generateAll(claude.generate, extract)

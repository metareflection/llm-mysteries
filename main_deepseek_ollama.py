import load
import deepseek
from extractor_ollama import extract
import re

def deepseek_extract(r, choices):
    pattern = r'<think>(.*)</think>'
    result = re.sub(pattern, lambda m: f'', r)
    return extract(result, choices)

if __name__ == '__main__':
    #load.generate1(deepseek.generate, deepseek_extract)
    load.generateAll(deepseek.generate, deepseek_extract)

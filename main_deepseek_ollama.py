import load
import deepseek_ollama
from extractor_ollama import extract
import re

def deepseek_extract(r, choices):
    pattern = r'<think>(.*)</think>'
    result = re.sub(pattern, lambda m: f'', r)
    return extract(result, choices)

if __name__ == '__main__':
    load.generateAll(deepseek_ollama.generate, deepseek_extract)

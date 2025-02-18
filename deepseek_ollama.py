import ollama

MODEL='deepseek-r1'
#MODEL='llama3.3'
#MODEL='phi4'

def generate(prompt):
    r = ollama.generate(model=MODEL, prompt=prompt, options={'temperature':0.6})
    response = r['response']
    return prompt+'\n'+response

if __name__ == '__main__':
    print(generate("What is 298396 * 7?"))

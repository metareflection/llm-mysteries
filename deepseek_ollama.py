import ollama

def generate(prompt):
    r = ollama.generate(model='deepseek-r1', prompt=prompt)
    response = r['response']
    return prompt+'\n'+response

if __name__ == '__main__':
    print(generate("What is 298396 * 7?"))

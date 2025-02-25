from load import dataset, suspects, culprit, tagline, story_text
from typing import Callable
import re
from claude import generate as claude_generate
import tqdm

buffer = ""

def log_wrapper(func: Callable=claude_generate):
    global buffer
    def wrapper(prompt: str) -> str:
        global buffer
        buffer += "\nPrompting: " + prompt + "\n"
        response = func(prompt)
        buffer += "\nResponse: " + response + "\n"
        return response
    return wrapper

default_generate_func = log_wrapper(claude_generate)


def extract_all_tags(text: str, tag: str) -> list[str]:
    """
    Extract all text between <tag> and </tag> in the given text. There can be multiple occurrences of the tag.
    """
    pattern = f'<{tag}>(.*?)</{tag}>'
    matches = re.findall(pattern, text, re.DOTALL)
    return matches

def detect_element(story_text: str, suspects: list[str], generate_func: Callable):
    prompt = "You are a detective. You are given a story and a list of suspects. You have to find all the potential elements that could be used against the suspects.\n\n"
    prompt += "The story is: {story_text}\n\n"
    prompt += "The suspects are: {suspects}\n\n"
    prompt += """
    Here are the few rule you need to follow:
    1. Before detecting the elements , you need to write your thoughts about the elements in the story in <think> and </think> tags.
    2. After that, you need to write the elements in <elements> and </elements> tags.
    3. The element should be organized in a chronological order.
    4. Do not make up any element that is not in the story.
    """
    prompt += "What are the potential element that could be used against the suspects?\n\n"
    prompt += "Answer:\n"

    prompt = prompt.format(story_text=story_text, suspects=str(suspects))

    response = generate_func(prompt)
    elements = extract_all_tags(response, 'elements')
    thoughts = extract_all_tags(response, 'think')
    return elements, thoughts


def associate_clue_between_elements(elements: list[str], suspects: list[str], generate_func: Callable) -> tuple[list[str], list[str]]:
    prompt = "You are a detective. You have collected some element and you need to associate the clues between the elements, and between the element and the suspects.\n\n"
    prompt += "The elements are: {elements}\n\n"
    prompt += "The suspects are: {suspects}\n\n"
    prompt += """
    Here are the few rule you need to follow:
    1. Before associating the clues, you need to write your thoughts about the clues in the element in <think> and </think> tags.
    2. After that, you need to write the clues in <clue> and </clue> tags.
    3. The clues should be organized in a chronological order.
    """
    prompt = prompt.format(elements=elements, suspects=str(suspects))

    response = generate_func(prompt)
    thoughts = extract_all_tags(response, 'think')
    clues = extract_all_tags(response, 'clue')
    return clues, thoughts


def answer_inspiration(story: str, elements: list[str], suspects: list[str], clues: list[str], memory: str, generate_func: Callable, max_tries=3):
    prompt = "You are a detective. You have collected some element, and you have to find the clues that could be used to inspire the suspects.\n\n"
    prompt += "The story is: {story}\n\n"
    prompt += "The elements are: {elements}\n\n"
    prompt += "The suspects are: {suspects}\n\n"
    prompt += "The clues are: {clues}\n\n"
    if memory:
        prompt += "So far, this is what you have thought: {memory}\n\n"
    prompt += """
    Here are the few rule you need to follow:
    1. Before answering, you need to write your thoughts about the clues in the element in <think> and </think> tags. Note that the lack of incriminating evidence does not directly imply innocence.
    2. When you think, if you find contradictory hypothesis, you need to write them in <contradictory> and </contradictory> tags and avoid these hypothesis. The contradictory hypothesis should be evidental and not just a guess. When you infer something, you have to cite the evidence from the story and element.
    3. After that, you need to write inspiration (i.e., abduction) in <inspiration> and </inspiration> tags.
    4. After finishing the inspiration, if you need to think more, write <continue>. Else, write <stop>.
    """
    prompt = prompt.format(story=story, elements=str(elements), suspects=str(suspects), clues=str(clues))

    response = generate_func(prompt)
    thoughts = extract_all_tags(response, 'think')
    contradictories = extract_all_tags(response, 'contradictory')
    inspirations = extract_all_tags(response, 'inspiration')
    stop = extract_all_tags(response, 'stop')
    continue_ = extract_all_tags(response, 'continue')
    if stop:
        return inspirations, thoughts, contradictories, True
    elif continue_ and max_tries > 0:
        return answer_inspiration(story, elements, suspects, clues, "Previous thoughts: "+ '\n'.join(thoughts) + "\n\nPrevious contradictories: " + '\n'.join(contradictories) + '\n\nPrevious Inspiration: ' + '\n'.join(inspirations), generate_func, max_tries-1)
    else:
        return inspirations, thoughts, contradictories, False


def answer(story: str, elements: list[str], suspects: list[str], clues: list[str], memory: str,
           thoughts: list[str], inspirations: str,
           contradictories: list[str],  generate_func: Callable):
    prompt = "You are a detective. You have collected some element, and you have to find the clues that could be used to inspire the suspects.\n\n"
    prompt += "The story is: {story}\n\n"
    prompt += "The elements are: {elements}\n\n"
    prompt += "The suspects are: {suspects}\n\n"
    prompt += "The clues are: {clues}\n\n"
    if memory:
        prompt += "So far, this is what you have thought: {memory}\n\n"
    if contradictories:
        prompt += "So far, this is what you contradictories you have inferred: {contradictories}\n\n"
    if thoughts:
        prompt += "So far, this is what you have thought: {thoughts}\n\n"
    if inspirations:
        prompt += "So far, this is what you have inspired: {inspirations}\n\n"
    prompt += """
    Here are the few rule you need to follow:
    1. Before answering, you need to write your thoughts about the clues in the element in <think> and </think> tags.
    2. When you think, if you find contradictory hypothesis, you need to write them in <contradictory> and </contradictory> tags and avoid these hypothesis. The contradictory hypothesis should be evidental and not just a guess. When you infer something, you have to cite the evidence from the story and element.
    3. After that, you need to write the answer in <answer> and </answer> tags.
    4. Write the final suspect and the suspect only in the tag <answer> and </answer>.
    """
    prompt = prompt.format(story=story, elements=elements, suspects=str(suspects), clues=str(clues), memory=memory, inspirations=inspirations, thoughts=thoughts, contradictories=contradictories)
    response = generate_func(prompt)
    thoughts = extract_all_tags(response, 'think')
    contradictories = extract_all_tags(response, 'contradictory')
    a = extract_all_tags(response, 'answer')
    if a:
        return a[0].strip(), thoughts, contradictories
    else:
        return "", thoughts, contradictories


if __name__ == '__main__':
    # Try the first case in the dataset
    tot = 0
    correct = 0
    buffer_fp = "log/claude_35_detect_bench.md"
    content = ""
    with open(buffer_fp, 'r') as f:
        content = f.read()
    # Find tot and correct
    new_content = ''
    for line in content.split("\n"):
        if "Found the real culprit" in line:
            correct += 1
            tot += 1
            bpos = new_content.rfind("<answer>")
            subcontent = new_content[bpos:]
            a = extract_all_tags(subcontent, 'answer')
            if a:
                line = "Found the real culprit: " + a[0].strip()
            new_content += line + "\n"
        elif "Found the wrong culprit" in line:
            real_culprit = line.split(":")[-1].strip().lower()
            wrong_culprit = line.split(":")[1].split(",")[0].strip().lower()
            if real_culprit.find(wrong_culprit) != -1 or wrong_culprit.find(real_culprit) != -1:
                correct += 1
                line = "Found the real culprit: " + wrong_culprit
            new_content += line + "\n"
            tot += 1
        else:
            new_content += line + "\n"
    content = new_content
    with open(buffer_fp, 'w') as f:
        f.write(content)
    # If there is no "Found the... from the last "Buffer:" then calculate it
    last_buffer = content.split("Buffer:")[-1]
    if "Found the real culprit" not in last_buffer and "Found the wrong culprit" not in last_buffer:
        a = extract_all_tags(last_buffer, 'answer')
        if a:
            x = dataset['train'][tot]
            cul = culprit(x)
            if a and a[0].strip() == cul.strip():
                correct += 1
            else:
                print(f"Found the wrong culprit: {answer}, not the real culprit: {cul}")
            tot += 1
    print(f"Found {correct} out of {tot} culprits.")
    with open(buffer_fp, 'a') as f:
        bar = tqdm.tqdm(enumerate(dataset['train']), total=len(dataset['train']))
        for i, x in bar:
            if i <= tot:
                continue
            suss = suspects(x)
            cul = culprit(x)
            st = story_text(x)
            elements, e_thoughts = detect_element(st, suss, default_generate_func)
            clues, c_thoughts = associate_clue_between_elements(elements, suss, default_generate_func)
            inspirations, i_thoughts, contradictories, stop = answer_inspiration(st, elements, suss, clues, "", default_generate_func)
            a, a_thoughts, a_contradictories = answer(st, elements, suss, clues, "", i_thoughts, inspirations, contradictories, default_generate_func)
            f.write(f"\nBuffer: \n{buffer}\n")
            if a == cul.strip():
                f.write(f"Found the real culprit: {a}")
                correct += 1
            else:
                f.write(f"Found the wrong culprit: {a}, not the real culprit: {cul}")
            tot += 1
            buffer = ""
            bar.set_description(f"Found {correct} out of {tot} culprits.")
    f.write(f"Found {correct} out of {tot} culprits.")

from load import dataset, suspects, culprit, tagline, story_text
from typing import Callable
import ollama
import re
from claude import generate as default_generate_func

# MODEL='deepseek-r1'
# default_generate_func = lambda prompt: ollama.generate(model=MODEL, prompt=prompt, options={'temperature':0.6})['respnose']

def extract_all_tags(text: str, tag: str) -> list[str]:
    """
    Extract all text between <tag> and </tag> in the given text. There can be multiple occurrences of the tag.
    """
    pattern = f'<{tag}>(.*?)</{tag}>'
    matches = re.findall(pattern, text, re.DOTALL)
    return matches

def detect_evidence(story_text: str, suspects: list[str], generate_func: Callable):
    prompt = "You are a detective. You are given a story and a list of suspects. You have to find all the potential evidence that could be used against the suspects.\n\n"
    "The story is: {story_text}\n\n"
    prompt += "The suspects are: {suspects}\n\n"
    prompt += """
    Here are the few rule you need to follow:
    1. Before detecting the evidence, you need to write your thoughts about the evidence in the story in <think> and </think> tags.
    2. After that, you need to write the evidence in <evidence> and </evidence> tags.
    3. The evidence should be organized in a chronological order.
    """
    prompt += "What are the potential evidence that could be used against the suspects?\n\n"
    prompt += "Answer:\n"

    prompt.format(story_text=story_text, suspects=str(suspects))

    response = generate_func(prompt)
    evidences = extract_all_tags(response, 'evidence')
    thoughts = extract_all_tags(response, 'think')
    return evidences, thoughts


def associate_clue_between_evidences(evidences: list[str], suspects: list[str], generate_func: Callable) -> tuple[list[str], list[str]]:
    prompt = "You are a detective. You have collected some evidence and you need to associate the clues between the evidences, and between the evidence and the suspects.\n\n"
    prompt += "The evidences are: {evidences}\n\n"
    prompt += "The suspects are: {suspects}\n\n"
    prompt += """
    Here are the few rule you need to follow:
    1. Before associating the clues, you need to write your thoughts about the clues in the evidence in <think> and </think> tags.
    2. After that, you need to write the clues in <clue> and </clue> tags.
    3. The clues should be organized in a chronological order.
    """
    prompt.format(evidences=evidences, suspects=str(suspects))

    response = generate_func(prompt)
    thoughts = extract_all_tags(response, 'think')
    clues = extract_all_tags(response, 'clue')
    return clues, thoughts


def answer_inspiration(story: str, evidences: list[str], suspects: list[str], clues: list[str], memory: str, generate_func: Callable, max_tries=3):
    prompt = "You are a detective. You have collected some evidence, and you have to find the clues that could be used to inspire the suspects.\n\n"
    prompt += "The story is: {story}\n\n"
    prompt += "The evidence is: {evidences}\n\n"
    prompt += "The suspects are: {suspects}\n\n"
    prompt += "The clues are: {clues}\n\n"
    if memory:
        prompt += "So far, this is what you have thought: {memory}\n\n"
    prompt += """
    Here are the few rule you need to follow:
    1. Before answering, you need to write your thoughts about the clues in the evidence in <think> and </think> tags.
    2. When you think, if you find contradictory hypothesis, you need to write them in <contradictory> and </contradictory> tags and avoid these hypothesis.
    3. After that, you need to write inspiration (i.e., abduction) in <inspiration> and </inspiration> tags.
    4. After finishing the inspiration, if you need to think more, write <continue>. Else, write <stop>.
    """
    prompt.format(story=story, evidences=str(evidences), suspects=str(suspects), clues=str(clues))

    response = generate_func(prompt)
    thoughts = extract_all_tags(response, 'think')
    contradictories = extract_all_tags(response, 'contradictory')
    inspirations = extract_all_tags(response, 'inspiration')
    stop = extract_all_tags(response, 'stop')
    continue_ = extract_all_tags(response, 'continue')
    if stop:
        return inspirations, thoughts, contradictories, True
    elif continue_ and max_tries > 0:
        return answer_inspiration(story, evidences, suspects, clues, "Previous thoughts: "+ '\n'.join(thoughts) + "\n\nPrevious contradictories: " + '\n'.join(contradictories) + '\n\nPrevious Inspiration: ' + '\n'.join(inspirations), generate_func, max_tries-1)
    else:
        return inspirations, thoughts, contradictories, False


def answer(story: str, evidences: list[str], suspects: list[str], clues: list[str], memory: str, inspirations: str, thoughts: list[str], contradictories: list[str],  generate_func: Callable):
    prompt = "You are a detective. You have collected some evidence, and you have to find the clues that could be used to inspire the suspects.\n\n"
    prompt += "The story is: {story}\n\n"
    prompt += "The evidence is: {evidence}\n\n"
    prompt += "The suspects are: {suspects}\n\n"
    prompt += "The clues are: {clues}\n\n"
    if memory:
        prompt += "So far, this is what you have thought: {memory}\n\n"
    if inspirations:
        prompt += "So far, this is what you have inspired: {inspirations}\n\n"
    if thoughts:
        prompt += "So far, this is what you have thought: {thoughts}\n\n"
    if contradictories:
        prompt += "So far, this is what you have thought: {contradictories}\n\n"
    prompt += """
    Here are the few rule you need to follow:
    1. Before answering, you need to write your thoughts about the clues in the evidence in <think> and </think> tags.
    2. When you think, if you find contradictory hypothesis, you need to write them in <contradictory> and </contradictory> tags and avoid these hypothesis.
    3. After that, you need to write the answer in <answer> and </answer> tags.
    4. Write the final suspect and the suspect only in the tag <answer> and </answer>.
    """
    prompt.format(story=story, evidences=evidences, suspects=str(suspects), clues=str(clues), memory=memory, inspirations=inspirations, thoughts=thoughts, contradictories=contradictories)
    r = generate_func(prompt)
    response = r['response']
    thoughts = extract_all_tags(response, 'think')
    contradictories = extract_all_tags(response, 'contradictory')
    answer = extract_all_tags(response, 'answer')
    if answer:
        return answer[0], thoughts, contradictories
    else:
        return "", thoughts, contradictories


if __name__ == '__main__':
    # Try the first case in the dataset
    for x in dataset:
        suss = suspects(x)
        cul = culprit(x)
        st = story_text(x)
        evidences, e_thoughts = detect_evidence(st, suss, default_generate_func)
        clues, c_thoughts = associate_clue_between_evidences(evidences, suss, default_generate_func)
        inspirations, i_thoughts, contradictories, stop = answer_inspiration(st, evidences, suss, clues, "", default_generate_func)
        answer, a_thoughts, a_contradictories = answer(st, evidences, suss, clues, "", inspirations, i_thoughts, contradictories, default_generate_func)
        print(f"Tagline: {tagline(x)}")
        print(f"Story: {st}")
        print(f"Suspects: {suss}")
        print(f"\n\nEvidences: {evidences}")
        print(f"\nE-Thoughts: {e_thoughts}")
        print(f"\n\nClues: {clues}")
        print(f"\nC-Thoughts: {c_thoughts}")
        print(f"\nInspirations: {inspirations}")
        print(f"\nI-Thoughts: {i_thoughts}")
        print(f"\nContradictories: {contradictories}")
        print(f"\n\nA-Thoughts: {a_thoughts}")
        print(f"\n\nAnswer Thoughts: {a_thoughts}")
        print(f"\n\nAnswer: {answer}")
        print(f"Real culprit: {cul}")
        if answer == cul:
            print("Found the real culprit!")
        else:
            print(f"Found the wrong culprit: {answer}, not the real culprit: {cul}")
        break

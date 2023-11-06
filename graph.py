
import llm
import extractor
from load import dataset, suspects, culprit

def generate_rest(msg):
    res = llm.generate(msg)
    return res[len(msg):]

bool_choices = ["No", "Yes"]

stats = {'found_none': 0, 'found': 0, 'not_found': 0, 'within': 0, 'not_within': 0}

def generate_node(s, qual, story, w=''):
    dir = f"{qual} evidence ({w}mean, {w}motive, {w}opportunity) for {s} in the story:"
    return generate_rest(f"Find {dir}\n{story}\nNow find {dir}")

def generate_nodes(ss, qual, story, w=''):
    return [generate_node(s, qual, story, w) for s in ss]

def generate_summary(ss, qual, nodes):
    return [extractor.gen(f"Possible {qual} evidence: {n}\nIs there {qual} strong evidence for {s}? Answer with Yes or No.", bool_choices) for (n,s) in zip(nodes,ss)]

def processCase(x):
    global stats
    print(f"## {x['comment']}")
    ss = suspects(x)
    story = x['input']
    incriminating_nodes = generate_nodes(ss, "incriminating", story)
    exonerating_nodes = generate_nodes(ss, "exonerating", story, w='no ')
    incriminating_summary = generate_summary(ss, "incriminating", incriminating_nodes)
    exonerating_summary = generate_summary(ss, "exonerating", exonerating_nodes)
    incriminating = [z=='Yes' for z in incriminating_summary]
    exonerating = [z=='Yes' for z in exonerating_summary]
    culprits = [y and (not n) for (y,n) in zip(incriminating, exonerating)]
    n_culprits = culprits.count(True)
    real_culprit = culprit(x)
    if n_culprits==0:
        print("Found no culprit. Real culprit {real_culprit}.")
        stats['found_none'] += 1
    elif n_culprits==1:
        index = culprits.index(True)
        found_culprit = ss[index]
        print(f"Found culprit {found_culprit}. Real culprit {real_culprit}.")
        stats['found' if found_culprit==real_culprit else 'not_found'] += 1
    else:
        print(f"Found {n_culprits} culprits out of {len(ss)} suspects.")
        index = ss.index(real_culprit)
        if culprits[index]:
            print(f"Including real culprit {real_culprit}.")
            stats['within'] += 1
        else:
            print(f"Excluding real culprit {real_culprit}.")
            stats['not_within'] += 1
    return x

if __name__ == '__main__':
    dataset.map(processCase)
    print(stats)

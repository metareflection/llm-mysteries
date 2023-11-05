import llm
import extractor
from load import dataset, suspects, culprit

def generate_rest(msg):
    res = llm.generate(msg)
    return res[len(msg):]

bool_choices = ["No", "Yes"]

stats = {'found': 0, 'not_found': 0, 'within': 0, 'not_within': 0}

def processCase(x):
    global stats
    print(f"## {x['comment']}")
    ss = suspects(x)
    story = x['input']
    incriminating_nodes = [generate_rest(f"Find incrinimating evidence (mean, motive, opportunity) for {s} in the following story. {story}") for s in ss]
    exonerating_nodes = [generate_rest(f"Find exonerating evidence (mean, motive, opportunity) for {s} in the following story. {story}") for s in ss]
    incriminating_summary = [extractor.gen(f"{n}\nBased on what precedes, is there incriminating evidence for {s}? Answer with Yes or No.", bool_choices) for (n,s) in zip(incriminating_nodes,ss)]
    exonerating_summary = [extractor.gen(f"{n}\nBased on what precedes, is there exonerating evidence for {s}? Answer with Yes or No.", bool_choices) for (n,s) in zip(exonerating_nodes,ss)]
    incriminating = [z=='Yes' for z in incriminating_summary]
    exonerating = [z=='Yes' for z in exonerating_summary]
    culprits = [y and (not n) for (y,n) in zip(incriminating, exonerating)]
    n_culprits = culprits.count(True)
    real_culprit = culprit(x)
    if n_culprits==0:
        print("Found no culprit.")
        stats['not_found'] += 1
    elif n_culprits==1:
        index = culprits.index(True)
        found_culprit = ss[index]
        print("Found culprit {found_culprit}. Real culprit {x}.")
        stats['found' if found_culprit==real_culprit else 'not_found'] += 1
    else:
        print("Found {n_culprit} culprits.")
        index = ss.index(real_culprit)
        if culprits[index]:
            print("Including real culprit.")
            stats['within'] += 1
        else:
            print("Excluding real culprit.")
            stats['not_within'] += 1
    return x

if __name__ == '__main__':
    dataset.map(processCase)
    print(stats)

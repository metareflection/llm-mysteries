#from tms_rc2 import TMS_RC2 as TMS
#from tms_rc2 import Xors
from tms_z3 import TMS_Z3X as TMS
from tms_z3 import Xors
from z3 import *
from math import prod

from mystery import story, parse

def label(id, what):
    return f"{id}-{what}"

def solve_all(story_lines):
    tms = TMS()
    whats = []
    story_suspects = []
    for line in story_lines:
        (id, what, val, confidence) = line
        probability = confidence if val else 1.0-confidence
        tms.create_node(label(id, what), probability=probability)
        if what not in whats:
            whats.append(what)
        if id not in story_suspects:
            story_suspects.append(id)
    suspect_nodes = [tms.create_node(id) for id in story_suspects]
    tms.add_constraint(
        "exactly one culprit",
        lambda xs: Xors(*xs),
        suspect_nodes)
    for (id,x) in zip(story_suspects, suspect_nodes):
        all_whats = [tms.node_by_label(label(id, what)) for what in whats]
        tms.add_constraint(
            f"soft constraint for guilty {id}",
            lambda xs: And(*xs),
            all_whats,
            probability=prod([tms.node_prob(x) for x in all_whats]))
        tms.add_constraint(
            f"all whats implies guilty for {id}",
            lambda xs: Implies(And(*xs[1:]), xs[0]),
            [x] + all_whats)
        tms.add_constraint(
            f"not all whats implies not guilty for {id}",
            lambda xs: Implies(Not(And(*xs[1:])), Not(xs[0])),
            [x] + all_whats)
    models = tms.maxsats()
    print('Belief changes:', tms.belief_changes())
    return set([guilty_party(model, story_suspects) for model in models])

def guilty_party(model, story_suspects):
    guilty = [id for id in story_suspects if model[id]]
    assert len(guilty) == 1
    return guilty[0]

def solve(story_lines):
    rs = solve_all(story_lines)
    if len(rs) > 1:
        print("WARNING: multiple top results", rs)
    return next(iter(rs))

if __name__ == '__main__':
    story_lines = story.split('\n')
    story_lines = [parse(line) for line in story_lines]
    print(solve(story_lines))

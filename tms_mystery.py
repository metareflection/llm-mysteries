from tms import TMS
from z3 import *

from mystery import whats, story, story_suspects, parse

def label(id, what, val):
    return f"{id}-{what}-{val}"

def solve(story_lines):
    tms = TMS()
    for line in story_lines:
        (id, what, val, confidence) = line
        tms.create_node(label(id, what, val), probability=confidence)
    suspect_nodes = [tms.create_node(id) for id in story_suspects]
    tms.add_constraint(
        "exactly one culprit",
        lambda xs: Sum([If(x, 1, 0) for x in xs]) == 1,
        suspect_nodes)
    for (id,x) in zip(story_suspects, suspect_nodes):
        for what in whats:
            tms.add_constraint(
                f"xor {id}-{what}",
                lambda xs: Xor(xs[0],xs[1]),
                [tms.node_by_label(label(id, what, True)),
                 tms.node_by_label(label(id, what, False))])
        all_whats = [tms.node_by_label(label(id, what, True))
                     for what in whats]
        tms.add_constraint(
            f"all whats implies guilty for {id}",
            lambda xs: Implies(And(*xs[1:]), xs[0]),
            [x] + all_whats)
        tms.add_constraint(
            f"not all whats implies not guilty for {id}",
            lambda xs: Implies(Not(And(*xs[1:])), Not(xs[0])),
            [x] + all_whats)
    model = tms.maxsat()
    return model

if __name__ == '__main__':
    story_lines = story.split('\n')
    story_lines = [parse(line) for line in story_lines]
    print(solve(story_lines))

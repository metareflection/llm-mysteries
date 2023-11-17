from math import exp
import re
from z3 import *

whats = ['mean', 'motive', 'opportunity']

story = """
Fiona Duncan has mean: she has her purse nearby!.
Fiona Duncan has opportunity: she goes to the bathroom!!.
Fiona Duncan has no motive: apparently.
Colonel Barrow has mean: he has big pockets!!.
Colonel Barrow has no mean: his coat is aside!!!.
Colonel Barrow has opportunity: he goes to the bathroom!!.
Colonel Barrow has no motive: he is a good fellow!!!.
Abby Grant has no mean: she wears a sleeveless dress!!!.
Abby Grant has opportunity: she is briefly absent!.
Abby Grant has motive: she likes necklaces as she wore won almost identical to the stolen one!!.
Harold Duncan has no mean: he didn't move!!!!!.
Harold Duncan has no opportunity: he didn't move!!!!!.
Harold Duncan has no motive: he is a good fellow!.
Maurice Eades has mean: he is a servant.
Maurice Eades has opportunity: he is a servant.
Maurice Eades has no motive: he is trusted!!!!!.
""".strip()

re_line = re.compile(r'(?P<id>\w+ \w+) has ((?P<neg>no) )?(?P<what>mean|opportunity|motive): (.*?)(?P<bangs>!*).')

def get_init(d, key):
    if key not in d:
        d[key] = {}
    return d[key]

def init_graph(story_lines):
    suspects = {}
    for line in story_lines:
        (id, what, val, confidence) = line
        d = get_init(suspects, id)
        d2 = get_init(d, what)
        d2[val] = confidence
    return suspects

def complete_graph(suspects):
    for (id,d) in suspects.items():
        for what in whats:
            for val in [True, False]:
                d2 = get_init(d, what)
                if val not in d2:
                    d2[val] = 0.0
    return suspects

def suspect_var(id):
    return f"{id} is guilty"

def what_var(id, what):
    return f"{id} has {what}"

def create_vars(suspects):
    vars = {}
    def add_var(s):
        vars[s] = Bool(s)
    for (id,d) in suspects.items():
        add_var(suspect_var(id))
        for what in whats:
            add_var(what_var(id, what))
    return vars

def add_soft_constraints(s, vars, suspects):
    for (id,d) in suspects.items():
        for what in whats:
           v = vars[what_var(id, what)]
           s.add_soft(Not(v), exp(-d[what][True]))
           s.add_soft(v, exp(-d[what][False]))

def add_hard_constraints(s, vars, suspects):
    xor_expr = Sum([If(vars[suspect_var(id)], 1, 0) for id in suspects.keys()]) == 1
    s.add(xor_expr)
    for (id,d) in suspects.items():
        var_id = vars[suspect_var(id)]
        all_whats = And(*[vars[what_var(id, what)] for what in whats])
        s.add(Implies(all_whats, var_id))
        s.add(Implies(Not(all_whats), Not(var_id)))

def find_guilty_suspect(model, vars, suspects):
    for id in suspects.keys():
        if model[vars[suspect_var(id)]]:
            return id
    assert False

def parse(line):
    m = re_line.fullmatch(line)
    assert m is not None
    id = m['id']
    what = m['what']
    val = True if m['neg'] is None else False
    confidence = len(m['bangs'])*0.2
    return (id, what, val, confidence)

def solve(story_lines):
    suspects = complete_graph(init_graph(story_lines))
    vars = create_vars(suspects)
    s = Optimize()
    add_soft_constraints(s, vars, suspects)
    add_hard_constraints(s, vars, suspects)
    assert s.check() == sat
    model = s.model()
    return find_guilty_suspect(model, vars, suspects)

if __name__ == '__main__':
    story_lines = story.split('\n')
    story_lines = [parse(line) for line in story_lines]
    print(solve(story_lines))

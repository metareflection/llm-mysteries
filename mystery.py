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

story_lines = story.split('\n')

re_line = re.compile(r'(?P<id>\w+ \w+) has ((?P<neg>no) )?(?P<what>mean|opportunity|motive): (.*?)(?P<bangs>!*).')

def get_init(d, key):
    if key not in d:
        d[key] = {}
    return d[key]

def init_graph(story_lines):
    suspects = {}
    for line in story_lines:
        m = re_line.fullmatch(line)
        assert m is not None
        id = m['id']
        d = get_init(suspects, id)
        what = m['what']
        d2 = get_init(d, what)
        val = True if m['neg'] is None else False
        confidence = len(m['bangs'])*0.2
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

suspects = complete_graph(init_graph(story_lines))

def create_vars(suspects):
    vars = {}
    def add_var(s):
        vars[s] = Bool(s)
    for (id,d) in suspects.items():
        add_var(f"{id} is guilty")
        for what in whats:
            add_var(f"{id} has {what}")
    return vars

vars = create_vars(suspects)


            

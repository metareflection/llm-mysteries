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

# returns the belief graph representing the beliefs for all the storylines
def init_graph(story_lines):
    suspects = {}
    for line in story_lines: # for each belief in the list of LLM's storylines
        (id, what, val, confidence) = line

        # when init_graph calls get_init with suspects, it creates just the suspect nodes for each suspect in the storylines, initializing suspects as keys and values as nested empty dictionaries
        d = get_init(suspects, id) # d is now a empty dictionary that is the value of what Character X is mapped to in the suspects dictionary

        # when init_graph calls get_init with d, it turns Character X's empty dictionary to be initialized with keys as each what node and values as empty dicts
        d2 = get_init(d, what) 

        # the confidence value for the current belief we are iterating on is updated in the 3rd layer of the graph, with the value being the max
        # of either the confidence of the current belief itself or the value (confidence) that was previously stored in the graph for a past belief -- if we have no
        # past beliefs, simply consider 0
        d2[val] = max(d2.get(val) or 0.0, confidence)
    return suspects

# takes in the initialized belief graph 
def complete_graph(suspects):
    for (id,d) in suspects.items():
        for what in whats:
            for val in [True, False]:
                d2 = get_init(d, what) # get the mapping of the confidences of True/False for the current what node we are on for the current suspect we are on
                if val not in d2: # we are iterating through True and False, so if either of those is not in the graph yet, set them to be 0 to make the graph structure complete
                    d2[val] = 0.0
    return suspects

def suspect_var(id):
    return f"{id} is guilty"

def what_var(id, what):
    return f"{id} has {what}"

# this function creates boolean variables representing if each suspect is guilty and for if each suspect has a given what node
def create_vars(suspects):
    vars = {}
    def add_var(s):
        vars[s] = Bool(s)


    for (id,d) in suspects.items():
        add_var(suspect_var(id)) # for each suspect, a variable is created like "Character X is guilty"
        for what in whats:
            add_var(what_var(id, what)) # For each 'what' of each suspect, a variable is created like "Character X has mean".

    # the strings are the keys and the values are the boolean variables representing the keys
    return vars

def add_soft_constraints(s, vars, suspects):
    for (id,d) in suspects.items():
        for what in whats:
           v = vars[what_var(id, what)] # v holds the boolean variable we defined for each what node variable

           # NOTE: be careful when thinking through this logic --> add_soft(arg, weight) --> means the Z3 model incurs the weight if it violates the argument
           # also note that we are raising e^(-negative confidence), so if the LLM has high confidence on a what node being true, the weight will be very low

           # so taking the inverse of the confidence/belief of a what node should be how much penalty is incurred if we violate the negation of the what node
           # since violating the negation of the what node is satisfying the what node itself --> high confidence/belief means low penalty in violating negation
           # while low confidence/belief means high peanlty for violating negation

           s.add_soft(Not(v), exp(-d[what][True])) 
           s.add_soft(v, exp(-d[what][False])) 

def add_hard_constraints(s, vars, suspects):
    # places an XOR constraint on all the suspects being guilty so that exactly 1 suspect is guilty
    xor_expr = Sum([If(vars[suspect_var(id)], 1, 0) for id in suspects.keys()]) == 1 
    s.add(xor_expr)

    # places a constraint such that if all of the what nodes for a suspect are true, then 'suspect is guilty' node is true -- meaning they are guilty
    # similarly, if all of the what nodes for a suspect are false, then 'suspect is not guilty node' is true -- meaning they are not guilty

    # perhaps this logic could be tweaked? Right now we assume that each what node has to be true for a suspect to be guilty, but will this be the case always? TODO: could play around with the constraints enforced here
    for (id,d) in suspects.items():
        var_id = vars[suspect_var(id)]
        all_whats = And(*[vars[what_var(id, what)] for what in whats])
        s.add(Implies(all_whats, var_id))
        s.add(Implies(Not(all_whats), Not(var_id)))

# Simply return the suspect for the suspect that is found guilty by the Z3 model
def find_guilty_suspect(model, vars, suspects):
    for id in suspects.keys():
        if model[vars[suspect_var(id)]]:
            return id
    assert False

# just printing
def show_interpretation(model, vars, suspects):
    for (id,d) in suspects.items():
        print(f"### {id}")
        for what in whats:
            tv = model[vars[what_var(id, what)]] # get the truth value as stored in the Z3 model
            print(f"- {what}: {tv} ({d[what][bool(tv)]})") # print the truth value from Z3 model and confidence (belief score) stored in nested belief graph from LLM output
        print("")

# This function isn't called by belief_graph.py --> used in main() for the sample story
def parse(line):
    m = re_line.fullmatch(line)
    assert m is not None
    id = m['id']
    what = m['what']
    val = True if m['neg'] is None else False
    confidence = len(m['bangs'])*0.2
    return (id, what, val, confidence)

# belief_graph.py calls this function, passing in all the storylines that the LLM has generated and its corresponding beliefs.
def solve(story_lines):
    # first creates a graph of all the storylines, with the graph being represented in nested dictionary format, then makes the graph complete with all the possible edges
    suspects = complete_graph(init_graph(story_lines))

    # create variables for each suspect's guilt and their what nodes, mapping them to a bool variable in the vars dict
    vars = create_vars(suspects)

    s = Optimize()

    # add constraints to the Z3 model, which is now stored in s
    add_soft_constraints(s, vars, suspects)
    add_hard_constraints(s, vars, suspects)
    assert s.check() == sat
    model = s.model()
    show_interpretation(model, vars, suspects)
    return find_guilty_suspect(model, vars, suspects) # solve and return


# this logic only operates on the sample story defined above for testing purposes, belief_graph.py never calls this
if __name__ == '__main__':
    story_lines = story.split('\n')
    story_lines = [parse(line) for line in story_lines]
    print(solve(story_lines))

    if False:
        import belief_graph
        print(belief_graph.solve(
            story,
            ['Fiona Duncan', 'Colonel Barrow', 'Abby Grant', 'Harold Duncan', 'Maurice Eades']
        ))

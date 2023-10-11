from extractor import gen

extra_prompt = "\nThe culprit is"

# 5minutemystery-who-let-the-frogs-out
prompt = """
The culprit is Locke.
There are two main clues.
1. Tom saw Locke leaving with his M-16.
2. Locke said he saw Buena Sera, Mrs. Campbell.
The movie Buena Sera, Mrs. Campbell was a 1968 comedy-drama film. The movie was set in Italy, not Vietnam.
The movie was not shown in Vietnam.
Therefore, Locke must have stolen the popcorn.
He ate it while watching the movie.
Locke is the culprit.
There are two main clues. 1. Tom saw Locke leaving with his M-16. 2. Locke said he saw Buena Sera, Mrs. Campbell. The movie Buena Sera, Mrs. Campbell was a 1968 comedy-drama film. The movie was set in Italy, not Vietnam. The movie was
"""
prompt += extra_prompt
choices = "Private First Class Dicky Mosier,Private Joe Locke,SpecialistFifth Class Ron Henson,Specialist Fourth Class Patrick Macnamara".split(",")
answer = gen(prompt, choices)
print(answer)
print("Should have been Private Joe Locke based on the prompt.")

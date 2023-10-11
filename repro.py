from extractor import gen

extra_prompt = "\nThe culprit is"

# 5minutemystery-who-let-the-frogs-out
prompt = """
Kyle Kravetsky
Sergio Ramos
Matilda Robbens
Mr. Womback
Marnie Pepper
The culprit is Marnie Pepper.
Mr. Womback locked the doors at 4:00 pm, and Kyle Kravetsky left the room at 5:00 pm, so Marnie Pepper is the only person who had the opportunity to open the doors and windows.
Mr. Womback locked the doors at 4:00 pm, and Kyle Kravetsky left the room at 5:00 pm, so Marnie Pepper is the only person who had the opportunity to open the doors and windows. Mr. Womback locked the doors at 4:00 pm, and Kyle Kravetsky left the room at 5:00 pm, so Marnie Pepper is the only person who had the opportunity to open the
"""
prompt += extra_prompt
choices = "Kyle Kravetsky,Marnie Pepper,Matilda Robbens,Sergio Ramos".split(",")
answer = gen(prompt, choices)
print(answer)
print("Should have been Marnie Pepper based on the prompt, even though it is in fact Matilda Robbens.")

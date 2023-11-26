from cot_example import example_story, example_solution_process

cot_example_for_prompt = 'The following is an example mystery story: \n' + example_story + ' \nThe following is an example reasoning process used to solve the mystery in the story: \n' + example_solution_process

preambule = cot_example_for_prompt + ' \n Here is a new mystery story. Your role is to find who is the culprit.'
postambule = 'Think step-by-step. Can you tell me who is the culprit?'
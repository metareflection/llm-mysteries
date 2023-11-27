# adapted from https://gist.github.com/brandonwillard/e1f41053c599bb584d4b922251cd96f5
import torch

import outlines.models as models

from outlines.text.generate.regex import choice
from outlines.text.generate.continuation import continuation
from outlines.text.generate.sample import greedy


# creates a custom text generator that uses a greedy strategy and tracks the cumulative log probability --> this is used to track the belief/confidence of generated text
# takes in parameters as a regular generator function that generate text and mask_token_ids that are tokens to focus on
# mask_token_ids is a optional parameter, but we pass in the tokens for True and False. If this parameter is not None, then we
# normalize the probabilities to focus on just those tokens
def make_greedy_tracker(generator, mask_token_ids=None):
    import types

    generator.sequence_log_prob = 0.0 #  track the cumulative log probability of the generated sequence.

    # this function replaces the generator's sampling method with a custom method, that is set to be a greedy strategy
    def tracking_greedy(
        logits: torch.DoubleTensor, samples: int, *_
    ) -> torch.DoubleTensor:
        next_token_ids = greedy(logits, samples)
        probs = torch.nn.functional.softmax(logits, dim=-1)
        if mask_token_ids:
            norm = sum([probs[:, id].squeeze() for id in mask_token_ids])
        else:
            norm = 1.0
        # TODO: hack!
        if norm < 0.01:
            norm = 1.0

        # add to the cumulative log probability
        generator.sequence_log_prob += torch.log(
            probs[:, next_token_ids.squeeze()].squeeze()/norm
        )
    

        return next_token_ids

    generator.sampler = tracking_greedy # assigns the sampling function of the generator to be the custom sampling we just defined

    def new_call(self, *args, **kwargs):
        # Reset the sequence log-probability to represent a new query to the LLM
        self.sequence_log_prob = 0.0 # TODO: does not seem to reset
        return super().__call__(*args, **kwargs)

    generator.__call__ = types.MethodType(generator, new_call)

    return generator


if __name__ == '__main__':
    model = models.transformers("gpt2")
    generator = make_greedy_tracker(continuation(model, max_tokens=50))
    choice_generator = make_greedy_tracker(
        choice(model, ["[Bb]lue", "[Rr]ed"], max_tokens=50)
    )
    prompt = "Which color do you prefer: blue or red?"

    sequence = generator(prompt)
    print(sequence)
    #
    #
    # The answer is blue.
    #
    # The color of the car is the color of the car.
    #
    # The color of the car is the color of the car.
    #
    # The color of the car is the color of the car.
    print(generator.sequence_log_prob)
    # tensor(-44.7725)


    sequence = choice_generator(prompt)
    print(sequence)
    # Blue
    print(choice_generator.sequence_log_prob)
    # tensor(-0.9262)

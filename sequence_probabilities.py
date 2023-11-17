import torch

import outlines.models as models

from outlines.text.generate.regex import choice
from outlines.text.generate.continuation import continuation
from outlines.text.generate.sample import greedy


def make_greedy_tracker(generator, mask_token_ids=None):
    import types

    generator.sequence_log_prob = 0.0

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
        generator.sequence_log_prob += torch.log(
            norm*probs[:, next_token_ids.squeeze()].squeeze()
        )

        return next_token_ids

    generator.sampler = tracking_greedy

    def new_call(self, *args, **kwargs):
        # Reset the sequence log-probability
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

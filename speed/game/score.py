

from speed.game.input_service import InputService


class Score:
    """Points earned. The responsibility of Score is to keep track of the player's points.

    Stereotype:
        Information Holder

    Attributes: 
        score: The user points.
    """

    def __init__(self) -> None:
        self.score = 0
        self.input_service = InputService()

    def increase_score(self, user_word):
        if user_word == self._word:
            self.score + 1
        else:
            self.score = self.score

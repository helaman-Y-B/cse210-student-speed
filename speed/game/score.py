
class Score():
    """Points earned. The responsibility of Score is to keep track of the player's points.

    Stereotype:
        Information Holder

    Attributes: 
        score: The user points.
    """

    def __init__(self):
        self._score = 0

        

    def increase_score(self, user_word, preset_word):
        if user_word == preset_word:
            self._score += 1

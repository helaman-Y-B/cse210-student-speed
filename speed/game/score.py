
class Score():
    """Points earned. The responsibility of Score is to keep track of the player's points.

    Stereotype:
        Information Holder

    Attributes: 
        score: The user points.
    """

    def __init__(self):
        """The constructor
        
        Args:
            self (Score): and instance of Score."""
        self._score = 0

    def increase_score(self):
        """Increases the score of the player.
        
        Args:
            self (Score): and instance of Score."""
        self._score += 1

    def _show_current_score(self):
        """Returns the current score of the user, to be displayed into the screen.
        
        Args:
            self (Score): and instance of Score."""
        return self._score

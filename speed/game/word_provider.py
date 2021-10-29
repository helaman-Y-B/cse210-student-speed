from speed.game.constants import LIBRARY
import random


class WordProvider:
    """The Class WordProvider, provides a random word from a list of words.

    Stereotype:
        Gameplay.

    Attributes:
        _word (Word): An Random word from a list."""

    def __init__(self) -> None:

        self._word = ""

    def word_picker(self):
        self._word = random.choice(LIBRARY)
        return self._word

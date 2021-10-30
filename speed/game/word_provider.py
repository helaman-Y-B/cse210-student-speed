from game.constants import LIBRARY
from game.point import Point
from game.constants import MAX_X, MAX_Y
import random


class WordProvider:
    """The Class WordProvider, provides a random word from a list of words.

    Stereotype:
        Gameplay.

    Attributes:
        _word (Word): An Random word from a list."""

    def __init__(self) -> None:

        self.point = Point()

        self._word = ""
        self._list_of_words = []

    def update_words(self):
        for _ in range(5):
            self._word = f"{self.get_words()}", self.point.get_new_x(
            ), self.point.get_new_y()
            self._list_of_words.append(self._word)
        return self._list_of_words

        # ~ new = self.point.move(words)

    def get_words(self):
        self.__random_word = random.choice(LIBRARY)
        return self.__random_word

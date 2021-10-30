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
        #self._word1 = "nicolas", self.point.get_new_x(), self.point.get_new_y()
        self._word = "", self.point.get_new_x(), self.point.get_new_y()
        #self._word2 = "james", self.point.get_new_x(), self.point.get_new_y()
        #self._word3 = "helama", self.point.get_new_x(), self.point.get_new_y()
        #self._word4 = "jhon", self.point.get_new_x(), self.point.get_new_y()
        #self._word5 = "joseph", self.point.get_new_x(), self.point.get_new_y()

    def word_picker(self):
        self._word = random.choice(LIBRARY)
        return self._word

    def update_words(self):
        for _ in range(5):
            self._word = f"{self.get_words()}", self.point.get_new_x(
            ), self.point.get_new_y()
            return self._word
        #self._word2 = "james", self.point.get_new_x(), self.point.get_new_y()
        #self._word3 = "helama", self.point.get_new_x(), self.point.get_new_y()
        #self._word4 = "jhon", self.point.get_new_x(), self.point.get_new_y()
        #self._word5 = "joseph", self.point.get_new_x(), self.point.get_new_y()

        # ~ new = self.point.move(words)

    def get_words(self):
        self.__random_word = random.choice(LIBRARY)
        return self.__random_word

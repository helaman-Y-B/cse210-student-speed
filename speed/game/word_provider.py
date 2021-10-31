from game.constants import LIBRARY
from game.point import Point
from game.constants import MAX_X, MAX_Y
import random


class WordProvider:
    """The Class WordProvider, provides a random word from a list of words.

    Stereotype:
        Gameplay.

    Attributes:
        point: the class Point.
        _word: a string.
        _word1: a word with coordinates.
        _word2: a word with coordinates.
        _word3: a word with coordinates.
        _word4: a word with coordinates.
        _word5: a word with coordinates.
        _word_state: a boolean value.
        """

    def __init__(self) -> None:
        """The constructor for the WordProvider class.
        
        Args:
            self (WordProvider): an instance of WorProvider."""

        self.point = Point()

        self._word1 = f"{self.word_picker()}", self.point.get_new_x(
        ), self.point.get_new_y()
        self._word2 = f"{self.word_picker()}", self.point.get_new_x(
        ), self.point.get_new_y()
        self._word3 = f"{self.word_picker()}", self.point.get_new_x(
        ), self.point.get_new_y()
        self._word4 = f"{self.word_picker()}", self.point.get_new_x(
        ), self.point.get_new_y()
        self._word5 = f"{self.word_picker()}", self.point.get_new_x(
        ), self.point.get_new_y()

        self._word_state = True
        self._word = ""

    def update_words(self):
        """Update the random generate words, so that it can appear in a different location.
        
        Args:
            self (WordProvider): an instance of WorProvider.
            
        returns a list of words."""
        
        if self._word_state:
            self._word1 = f"{self.get_words()[0]}", self.point.get_new_x(
            ), self.point.get_new_y()
            self._word2 = f"{self.get_words()[1]}", self.point.get_new_x(
            ), self.point.get_new_y()
            self._word3 = f"{self.get_words()[2]}", self.point.get_new_x(
            ), self.point.get_new_y()
            self._word4 = f"{self.get_words()[3]}", self.point.get_new_x(
            ), self.point.get_new_y()
            self._word5 = f"{self.get_words()[4]}", self.point.get_new_x(
            ), self.point.get_new_y()

        words = self._word1, self._word2, self._word3, self._word4, self._word5

        return words

    def word_picker(self):
        """Selects a random word from a list.
        
        Args:
            self (WordProvider): an instance of WorProvider.
            
        Returns a random word."""
        self._word = random.choice(LIBRARY)
        return self._word

    def get_words(self):
        """Makes a list of ONLY words.
        
        Args:
            self (WordProvider): an instance of WorProvider."""
        
        words = self._word1[0], self._word2[0], self._word3[0], self._word4[0], self._word5[0]
        return words

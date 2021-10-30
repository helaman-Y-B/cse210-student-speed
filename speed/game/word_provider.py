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
        self._word1 = "nicolas", self.point.get_new_x(), self.point.get_new_y()
        self._word2 = "james", self.point.get_new_x(), self.point.get_new_y()
        self._word3 = "helama", self.point.get_new_x(), self.point.get_new_y()
        self._word4 = "jhon", self.point.get_new_x(), self.point.get_new_y()
        self._word5 = "joseph", self.point.get_new_x(), self.point.get_new_y()
        
        

    def word_picker(self):
        self._word = random.choice(LIBRARY)
        return self._word
        
    def update_words(self):
        
        self._word1 = "nicolas", self.point.get_new_x(), self.point.get_new_y()
        self._word2 = "james", self.point.get_new_x(), self.point.get_new_y()
        self._word3 = "helama", self.point.get_new_x(), self.point.get_new_y()
        self._word4 = "jhon", self.point.get_new_x(), self.point.get_new_y()
        self._word5 = "joseph", self.point.get_new_x(), self.point.get_new_y()


        
        
        words =  self._word1, self._word2, self._word3, self._word4, self._word5
        
        # ~ new = self.point.move(words)
        
        return words
        
    def get_words(self):
        words = self._word1[0], self._word2[0], self._word3[0], self._word4[0], self._word5[0]
        return words
        

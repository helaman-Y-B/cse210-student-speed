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
        self._word1 = ""
        self._word2 = ""
        self._word3 = ""
        self._word4 = ""
        self._word5 = ""
        self.word1_state = True
        self.word2_state = True
        self.word3_state = True
        self.word4_state = True
        self.word5_state = True
        self.name1 = "nicolas"
        self.name2 = "james"
        self.name3 = "helama"
        self.name4 = "jhon"
        self.name5 = "joseph"
        
        

    def word_picker(self):
        self._word = random.choice(LIBRARY)
        return self._word
        
    def update_words(self):
        
        if self.word1_state: self._word1 = self.name1, self.point.get_new_x(), self.point.get_new_y()
        if self.word2_state: self._word2 = self.name2, self.point.get_new_x(), self.point.get_new_y()
        if self.word3_state: self._word3 = self.name3, self.point.get_new_x(), self.point.get_new_y()
        if self.word4_state: self._word4 = self.name4, self.point.get_new_x(), self.point.get_new_y()
        if self.word5_state: self._word5 = self.name5, self.point.get_new_x(), self.point.get_new_y()


        
        
        words =  self._word1, self._word2, self._word3, self._word4, self._word5
        
        # ~ new = self.point.move(words)
        
        return words
        
    def get_words(self):
        words = self.name1, self.name2, self.name3, self.name4, self.name5
        return words
        
    def clean_word(self, word):
        
        if word in self._word1:
            self._word1 = "",0,0
            self.word1_state = False 
        if word in self._word2:
            self._word2 = "",0,0
            self.word2_state = False
        if word in self._word3:
            self._word3 = "",0,0
            self.word3_state = False
        if word in self._word4:
            self._word4 = "",0,0
            self.word4_state = False
        if word in self._word1:
            self._word5 = "",0,0
            self.word5_state = False

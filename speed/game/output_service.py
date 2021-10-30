from game.constants import MAX_X, MAX_Y
from game.point import Point
from game.word_provider import WordProvider


class OutputService:
    """The OutputService send the word that the user needs to type.

    Stereotype:
        Service Provider

    Attributes:
        _screen (Screen): An Asciimatics screen."""

    def __init__(self, screen):
        """The class constructor.

        Args:
            self (OutputService): An instance of OutputService.
            screen (Screen): An Asciimatics Screen.
        """
        self._screen = screen
        self.point = Point()
        self.word = WordProvider()
        self.words_init = self.word.get_words()
        

    def clear_screen(self):
        """Clears the Asciimatics buffer in preparation for the next rendering.

        Args:
            self (OutputService): An instance of OutputService.
        """
        self._screen.clear_buffer(7, 0, 0)
        self._screen.print_at("-" * MAX_X, 0, 0, 7)
        self._screen.print_at("-" * MAX_X, 0, MAX_Y, 7)
        
    def draw_interface(self, interface):
        text1, x1, y1 = interface.get_score()

        text2, x2, y2= interface.get_buffer()

        
        self._screen.print_at(text1, x1, y1, 7)
        self._screen.print_at(text2, x2, y2, 7)
        
    def draw_word(self):
         for i in self.word.update_words():
            word, x, y = i 
            if len(word) > 0:
                self._screen.print_at(word, x, y, 7)
            
    def get_words(self):
        
        words = []
        for i in self.word.get_words():
            if len(i) > 0:
                words.append(i)
        return words
    
    def get_init_words(self):
        
        return self.words_init

            
        
    def clean(self, word):
        self.word.clean_word(word)
        




    def flush_buffer(self):
        """Renders the screen.

        Args:
            self (OutputService): An instance of OutputService.
        """
        self._screen.refresh()

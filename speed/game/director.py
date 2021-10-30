# ~ from game.input_service import InputService
from game.score import Score
# ~ from game.word_provider import WordProvider
from game.interface import Interface
from game import constants
from time import sleep


class Director:
    """The Director class directs the data to each class from the game in an order,
    so that the game can continue.

    Stereotype:
        Controller

    Attributes:
        _word: The word that the user needs to type."""

    def __init__(self, input_service, output_service):
        # ~ self._word = WordProvider()
        self._score = Score()
        self._keep_playing = True
        self._output_service = output_service
        self._input_service = input_service
        self._interface = Interface()
        

    def start_game(self):
        while self._keep_playing:
            self._get_input()
            self._get_outputs()
            self._do_updates()
            sleep(0.5)

    def _get_input(self):
        pass
        # ~ letter = self._input_service.get_letter()
        # ~ self._interface.set_buffer(letter, self._output_service.get_words())
        
        # ~ self._word.clean_word(self._interface.get_word())
        

    def _do_updates(self):
        letter = self._input_service.get_letter()
        self._interface.set_buffer(letter, self._output_service.get_init_words())
        self._output_service.clean(self._interface.get_word())

    def _get_outputs(self):
        self._output_service.clear_screen()
        self._output_service.draw_interface(self._interface)
        self._output_service.draw_word()
        # ~ self._output_service.draw_actors()
        self._output_service.flush_buffer()

# ~ from game.input_service import InputService
from game.word_provider import WordProvider
from game.interface import Interface
from time import sleep


class Director:
    """The Director class directs the data to each class from the game in an order,
    so that the game can continue.

    Stereotype:
        Controller

    Attributes:
        self._word: The word that the user needs to type.
        self._keep_playing: A boolean valu to keep the game running.
        self._output_service: which gets the output from the output_service class.
        self._input_service: which gets the input from the input_service class.
        self._interface: Which gets the interface class."""

    def __init__(self, input_service, output_service):
        """The constructor function"""
        self._word = WordProvider()
        self._keep_playing = True
        self._output_service = output_service
        self._input_service = input_service
        self._interface = Interface()

    def start_game(self):
        """The start_game function do exacly what it says... it starts the game,
        by calling the get_input function and the get_output function."""
        #While keep playing iquals to true.
        while self._keep_playing:
            #call the functions
            self._get_input()
            self._get_outputs()
            #We called sleep to make the game happen during each one second.
            sleep(1.0)

    def _get_input(self):
        """The _get_input function directs the input data from the user to the other classes."""
        #letter gets the letter the user just typed
        letter = self._input_service.get_letter()
        #after we set the buffer
        self._interface.set_buffer(letter, self._output_service.get_words())
        #and after gets the buffer
        self._interface.get_buffer()

    def _get_outputs(self):
        """The class _get_output shows the output screen and data to the user."""
        self._output_service.clear_screen()#shows a clear screen
        self._output_service.draw_interface(self._interface)#Draws the interface of the game
        self._output_service.draw_word()#draw the word
        self._output_service.flush_buffer()#Flush the buffer

from boggle_logic import Boggle 
from gui import Game as MainScreen
from open_screen import OpeningScreen
from end_screen import EndScreen

class GamePlay:
    """
    Represents the game play functionality of a Boggle game.

    Attributes:
        __game (Boggle): The Boggle game instance.

    Methods:
        play(): Executes the game loop.
        show_end_screen(): Displays the end screen of the game.
        __init__(): Initializes the GamePlay object.
        __first_screen(): Displays the opening screen of the game.
        __run_game(): Executes the main game logic.
    """

    def __init__(self) -> None:
        """
        Initializes a new instance of the GamePlay class.
        """
        self.__game=Boggle()
        
    def play(self):
        """
        Executes the game loop.

        This method runs the game continuously until the player chooses to exit.
        """
        self.__first_screen()
        while True:
            self.__run_game()
            self.show_end_screen()
            
    def show_end_screen(self):
        """
        Displays the end screen of the game.

        This method creates an EndScreen instance and runs it to show the game results.
        """
        end_screen=EndScreen(self.__game)
        end_screen.run()
        
    def __first_screen(self):
        """
        Displays the opening screen of the game.

        This method creates an OpeningScreen instance and runs it to show the game's initial screen.
        """
        first_screen=OpeningScreen()
        first_screen.run()

    def __run_game(self):
        """
        Executes the main game logic.

        This method starts the game, creates a MainScreen instance, and runs it to handle the game's core gameplay.
        """
        self.__game.start_game()
        main_screen=MainScreen(self.__game)
        main_screen.run()
    


if __name__ == "__main__":    
    game_play=GamePlay()
    game_play.play()
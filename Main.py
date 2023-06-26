from boggle_logic import Boggle 
from gui import Game as MainScreen
from open_screen import OpeningScreen
from end_screen import EndScreen

class GamePlay:
    def __init__(self) -> None:
        self.__game=Boggle()
        
    def play(self):
        self.__first_screen()
        while True:
            self.__run_game()
            self.show_end_screen()
            
    def show_end_screen(self):
        end_screen=EndScreen(self.__game)
        end_screen.run()
        
    def __first_screen(self):
        first_screen=OpeningScreen()
        first_screen.run()

    def __run_game(self):
        self.__game.start_game()
        main_screen=MainScreen(self.__game)
        main_screen.run()
    


if __name__ == "__main__":    
    game_play=GamePlay()
    game_play.play()
from boggle import Boggle 
from gui import Game as MainScreen
from open_screen import OpeningScreen


def main():
    first_screen()
    run_game()

def first_screen():
    first_screen=OpeningScreen()
    first_screen.run()

def run_game():
    game=Boggle()
    game.start_game()
    main_screen=MainScreen(game)
    main_screen.run()
    


if __name__ == "__main__":    
    main()
import tkinter as tk
from boggle_logic import Boggle

TITLE = "Boggle"
END_GOOD_STRING = "GOOD GAME!"
END_BAD_STRING = "WELL PLAYED,\n NEXT TIME YOU WILL BE BETTER"
PLAY_AGAIN = "Play again?"
EXIT = "Exit"


class EndScreen:
    def __init__(self, game: Boggle):
        """init end screen"""
        self.__game = game
        self.__create_page()
        # self.__start_events:list=list()

    def __create_page(self):
        """Create the screen"""
        self.__root = tk.Tk()
        self.__root.title(TITLE)
        self.__root.geometry("500x400")  # Set the width and height of the window
        self.__create_score_text()
        self.__create_text()
        self.__create_buttons()
        self.__create_used_words_label()
        self.__root.protocol("WM_DELETE_WINDOW", self.on_closing)

    def on_closing(self):
        """Close"""
        quit()

    def __create_text(self):
        """Create the upper text and adjust by the score"""
        self.__label_text = tk.Label(
            self.__root, font=("Arial", 24))
        if self.__game.score > 20:
            self.__label_text.config(text=END_GOOD_STRING)
        else:
            self.__label_text.config(text=END_BAD_STRING)
            self.__label_text.config(font=("Arial", 18))
        self.__label_text.pack(pady=20)

    def __create_score_text(self):
        """Creates the text score and show the score that the player got"""
        self.__label_score_text = tk.Label(
            self.__root, text="Your score is {:2d}".format(self.__game.score), font=("Arial", 24))
        self.__label_score_text.pack(pady=10)

    def __create_buttons(self):
        """Create the play again button"""
        self.__start_button = tk.Button(
            self.__root, text=PLAY_AGAIN, font=("Arial", 24), command=self.start_game)
        self.__start_button.pack(pady=10, padx=10)
        self.__start_button.place(relx=0.5, rely=0.5, anchor='center')

    def __create_used_words_label(self):
        self.__label_score_text = tk.Label(
            self.__root, font=("Arial", 16))
        self.__label_score_text.config(text="The words that you found:\n" + self.__game.used_words_to_string())
        self.__label_score_text.pack(pady=40, side=tk.BOTTOM)

    def start_game(self):
        """Start game method"""
        self.close_window()

    def close_window(self):
        """Close window"""
        self.__root.destroy()

        # self.__root.destroy()

    def run(self):
        """Run the root of end screen"""
        self.__root.mainloop()


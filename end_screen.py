import tkinter as tk
from boggle_logic import Boggle

TITLE="Boggle"
END_GOOD_STRING="GOOD GAME!"
END_BAD_STRING="WELL PLAYED,\n NEXT TIME YOU WILL BE BETTER"
PLAY_AGAIN="Play again?"
EXIT="Exit"

class EndScreen:
    def __init__(self,game:Boggle):
        self.__game=game
        self.__create_page()
        # self.__start_events:list=list()

    def __create_page(self):
        self.__root = tk.Tk()
        self.__root.title(TITLE)
        self.__root.geometry("500x400")  # Set the width and height of the window
        self.__create_score_text()
        self.__create_text()
        self.__create_buttons()
        self.__root.protocol("WM_DELETE_WINDOW", self.on_closing)
    
    def on_closing(self):
        quit()

    def __create_text(self):
        self.__label_text = tk.Label(
            self.__root, font=("Arial", 24))
        if self.__game.score > 20:
            self.__label_text.config(text=END_GOOD_STRING)
        else:
            self.__label_text.config(text=END_BAD_STRING)
            self.__label_text.config(font=("Arial", 18))
        self.__label_text.pack(pady=20)
    def __create_score_text(self):
        self.__label_score_text = tk.Label(
            self.__root, text="Your score is {:2d}".format(self.__game.score), font=("Arial", 24))
        self.__label_score_text.pack(pady=10)
    def __create_buttons(self):
        self.__start_button = tk.Button(
            self.__root, text=PLAY_AGAIN, font=("Arial", 24), command=self.start_game)
        self.__start_button.pack(pady=10,padx=10)
        self.__start_button.place(relx=0.5, rely=0.5, anchor='center')


        
    def start_game(self):  
        self.close_window()
        
    def close_window(self):
        self.__root.destroy()
    
        # self.__root.destroy()

    def run(self):
        self.__root.mainloop()


if __name__ == '__main__':
    opening_screen = EndScreen(None)
    opening_screen.run()


import tkinter as tk
import time

TITLE="Boggle"
OPENING_STRING="GOOD GAME!"
PLAY_AGAIN="Play again?"
EXIT="Exit"

class EndScreen:
    def __init__(self,game):
        self.__create_page()
        self.__game=game
        # self.__start_events:list=list()

    def __create_page(self):
        self.__root = tk.Tk()
        self.__root.title(TITLE)
        self.__root.geometry("500x400")  # Set the width and height of the window
        self.__create_text()
        self.__create_score_text()
        self.__create_buttons()
        self.__root.protocol("WM_DELETE_WINDOW", self.on_closing)
    
    def on_closing(self):
        quit()

    def __create_text(self):
        self.__label_text = tk.Label(
            self.__root, text=OPENING_STRING, font=("Arial", 24))
        self.__label_text.pack(pady=20)
    def __create_score_text(self):
        self.__label_score_text = tk.Label(
            self.__root, text="Your score is {:2d}".format(25), font=("Arial", 24))
        self.__label_score_text.pack(pady=20)
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


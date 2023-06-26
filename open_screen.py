import tkinter as tk
import time

TITLE="Boggle"
OPENING_STRING="WELCOME TO BOGGLE"
START="Start"
EXIT="Exit"
class OpeningScreen:
    def __init__(self):
        self.__create_page()


    def __create_page(self):
        self.__root = tk.Tk()
        self.__root.title(TITLE)
        self.__root.geometry("500x400")  # Set the width and height of the window
        self.__create_text()
        self.__create_buttons()
      

    def __create_text(self):
        self.__label_text = tk.Label(
            self.__root, text=OPENING_STRING, font=("Arial", 24))
        self.__label_text.pack(pady=20)

    def __create_buttons(self):
        self.__start_button = tk.Button(
            self.__root, text=START, font=("Arial", 24), command=self.start_game)
        self.__start_button.pack(pady=10,padx=10)
        self.__start_button.place(relx=0.5, rely=0.5, anchor='center')


    def start_game(self):
        pass

    def run(self):
        self.__root.mainloop()


if __name__ == '__main__':
    opening_screen = OpeningScreen()
    opening_screen.run()


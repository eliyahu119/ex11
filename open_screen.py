import tkinter as tk
import time

TITLE="Boggle"
OPENING_STRING="WELCOME TO BOGGLE"
START="Start"
EXIT="Exit"
class OpeningScreen:
    def __init__(self):
        """Init the open screen"""
        self.__create_page()
        self.__start_events:list=list()

    def __create_page(self):
        """Create the screen"""
        self.__create_root()
        self.__create_text()
        self.__create_buttons()
        self.__root.protocol("WM_DELETE_WINDOW", self.on_closing)
    
    def on_closing(self):
        """On closing"""
        quit()
    def __create_root(self):
        """Create the root"""
        self.__root = tk.Tk()
        self.__root.title(TITLE)
        self.__root.geometry("500x400")  # Set the width and height of the window
    def __create_text(self):
        """Create the open text"""
        self.__label_text = tk.Label(
            self.__root, text=OPENING_STRING, font=("Arial", 24))
        self.__label_text.pack(pady=20)

    def __create_buttons(self):
        """Create the Start button"""
        self.__start_button = tk.Button(
            self.__root, text=START, font=("Arial", 24), command=self.start_game)
        self.__start_button.pack(pady=10,padx=10)
        self.__start_button.place(relx=0.5, rely=0.5, anchor='center')

    def add_events_to_start(self, func):
        """Add events"""
        self.__start_events.append(func)
        
    def start_game(self):
        """Start game"""
        self.close_window()
        
    def close_window(self):
        """Close window"""
        self.__root.destroy()
    
    def run(self):
        """Run"""
        self.__root.mainloop()


if __name__ == '__main__':
    opening_screen = OpeningScreen()
    opening_screen.run()


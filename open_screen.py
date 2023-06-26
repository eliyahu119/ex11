import tkinter as tk

class OpeningScreen:
    def __init__(self):
        self.__create_page()
        self.__run()
    def __create_page(self):
        self.__root = tk.Tk()
        self.__root.title("Boggle")
        self.__create_text()
        self.__create_buttons()
        self.__create_emoji()
    def __create_text(self):
            self.__label_text = tk.Label(self.__root, text="Do you want to Play", font=("Arial", 24))
            self.__label_text.pack(pady=20)
    def __create_buttons(self):
            self.__start_button = tk.Button(self.__root, text="Start", font=("Arial", 16), command=self.start_game)
            self.__start_button.pack(pady=10)

            self.__exit_button = tk.Button(self.__root, text="Exit", font=("Arial", 16), command=self.__root.quit)
            self.__exit_button.pack(pady=10)
    def __create_emoji(self):
        self.__emoji_image = tk.PhotoImage(file="emoji.png")
        self.__label_emoji = tk.Label(self.__root, image=self.__emoji_image)
        self.__label_emoji.pack(pady=20)
    def start_game(self):
        pass

    def __run(self):
        self.__root.mainloop()

if __name__ == '__main__':
    opening_screen = OpeningScreen()


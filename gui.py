import string
from typing import Dict, List, Callable, Any
import tkinter as tk
import time

from boggle import Boggle

ROOT_NAME = "Boggle"
BUTTON_HOVER_COLOR = 'gray'
REGULAR_COLOR = 'lightgray'
BUTTON_ACTIVE_COLOR = 'slateblue'
##TEST
BUTTON_STYLE = {"font": ("Courier", 30),
                "borderwidth": 1,
                "relief": tk.RAISED,
                "bg": REGULAR_COLOR,
                "activebackground": BUTTON_ACTIVE_COLOR}
ROWS =4
COLS=4
class Game:
    def __init__(self,boggle:Boggle):   #basic init
        self.__boggle=boggle
        self.__boggle.start_game()
        self.__current_word = ""
        self.create_gui()

#---------------------------------create all formats
    #create all
    def create_gui(self):
        self.__root = tk.Tk()
        self.__root.title(ROOT_NAME)
        self.create_upper_frame()
        self.create_display_label()
        self.create_buttons_grid(self.__boggle)
        self.create_buttom_format()

    # Create a timer and score frame
    def create_upper_frame(self):
        self.upper_frame = tk.Frame(self.__root)
        self.upper_frame.pack(pady=10, fill=tk.BOTH)

        self.timer_label = tk.Label(self.upper_frame, text="", font=("Helvetica", 24, "bold"), justify='l')
        self.timer_label.pack(side=tk.LEFT)

        self.score_label = tk.Label(self.upper_frame, text="score: 0", font=("Helvetica", 24, "bold"), justify='r')
        self.score_label.pack(side=tk.RIGHT)

    # create a label for word
    def create_display_label(self):
        self._display_label = tk.Label(self.__root, font=("Courier", 30),
                                       bg="lightgray", width=23, relief="ridge")
        self._display_label.pack(side=tk.TOP, fill=tk.BOTH)

    # create a frame for buttons
    def create_buttons_grid(self,table):
        self.button_grid_frame = tk.Frame(self.__root)
        self.button_grid_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        self.create_buttons_in_lower_frame()


    # create buttom format
    def create_buttom_format(self):
        self.buttom_frame = tk.Frame(self.__root)
        self.buttom_frame.pack(fill=tk.BOTH)

        self.save_word_button = tk.Button(self.buttom_frame,**BUTTON_STYLE,text= "Save\nword",command= self.save_word)
        self.save_word_button.pack(side=tk.LEFT)

        self.used_words = tk.Label(self.buttom_frame,justify='l',text = "",font=("Courier", 8),
                                       bg="lightgray", width=23, relief="ridge")
        self.used_words.pack(side=tk.LEFT,fill=tk.BOTH,expand='true')

    def save_word(self):
        self.__boggle.submit_word()
        self.__current_word = ""
        self.update_current_word()
        self.update_score()
        self.update_used_words_screen()
#-------------------------------------------------#
    #timer
    def update_timer(self):
        remaining_time = self.__boggle.get_current_time()
        if remaining_time > 0:
            minutes = int(remaining_time // 60)
            seconds = int(remaining_time % 60)
            self.timer_label.config(text="time: {:02d}:{:02d}".format(minutes, seconds))
            self.timer_label.after(1000, self.update_timer)
        else:
            self.__root.destroy()
    def update_score(self):
        self.score_label.config(text= "score:{:2d}".format(self.__boggle.score))

    def update_used_words_screen(self):
        str = ""
        lst = self.__boggle.used_words
        for word in lst:
            str += word
            str += " "
        self.used_words.config(text=str)

    #run methos(incomplete)
    def run(self):
        self.update_timer()
        self.__root.mainloop()

#---------------------------------buttons grid and button settings


    def create_buttons_in_lower_frame(self) -> None:
        #create grid table
        for i in range(COLS):
            tk.Grid.columnconfigure(self.button_grid_frame, i, weight=1)  # type: ignore

        for i in range(ROWS):
            tk.Grid.rowconfigure(self.button_grid_frame, i, weight=1)  # type: ignore
        self.grid_buttons = []

        for row in range(ROWS):
            row_buttons = []
            for col in range(COLS):
                #create button and place in grid
                button = tk.Button(self.button_grid_frame, text=self.__boggle.get_value_by_location(row,col).upper(),
                                   **BUTTON_STYLE, command= lambda r=row,c=col: self.grid_button_click(r,c))
                button.grid(row=row, column=col, sticky=tk.NSEW)
                #make buttons shine if mouse on him
                self.change_button_color_on_hover(button,BUTTON_HOVER_COLOR,REGULAR_COLOR)
                #append button
                row_buttons.append(button)
            self.grid_buttons.append(row_buttons)

    def grid_button_click(self,x,y):
        self.__boggle.add_to_current_path(x,y)
        self.__current_word += self.__boggle.get_value_by_location(x,y)
        self.update_current_word()

    def update_current_word(self):
        self._display_label.config(text=self.__current_word)
    #make button shine when mouse on him
    def change_button_color_on_hover(self,button, hover_color, regular_color):
        def on_enter(event):
            button.config(background=hover_color)

        def on_leave(event):
            button.config(background=regular_color)

        button.bind("<Enter>", on_enter)
        button.bind("<Leave>", on_leave)
#--------------------------------------------------------

if __name__ == '__main__':
    b = Boggle()
    a = Game(b)
    a.run()
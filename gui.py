import string
from typing import Dict, List, Callable, Any
import tkinter as tk
import time
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
    buttons: Dict[str, tk.Button] = {}
    def __init__(self,table):   #basic init
        self.duration =180
        self.root = tk.Tk()
        self.root.title(ROOT_NAME)
        self.table=table

        self.create_gui()
#---------------------------------create all formats
    #create all
    def create_gui(self):
        self.create_upper_frame()
        self.create_display_label()
        self.create_buttons_grid(self.table)
        self.create_buttom_format()

    # Create a timer and score frame
    def create_upper_frame(self):
        self.upper_frame = tk.Frame(self.root)
        self.upper_frame.pack(pady=10, fill=tk.BOTH)

        self.timer_label = tk.Label(self.upper_frame, text="", font=("Helvetica", 24, "bold"), justify='l')
        self.timer_label.pack(side=tk.LEFT)

        self.score_label = tk.Label(self.upper_frame, text="x", font=("Helvetica", 24, "bold"), justify='r')
        self.score_label.pack(side=tk.RIGHT)

    # create a label for word
    def create_display_label(self):
        self._display_label = tk.Label(self.root, font=("Courier", 30),
                                       bg="lightgray", width=23, relief="ridge")
        self._display_label.pack(side=tk.TOP, fill=tk.BOTH)

    # create a frame for buttons
    def create_buttons_grid(self,table):
        self.button_grid_frame = tk.Frame(self.root)
        self.button_grid_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        self.create_buttons_in_lower_frame(table)
        self.root.bind("<Key>", self._key_pressed)

    # create buttom format
    def create_buttom_format(self):
        self.buttom_frame = tk.Frame(self.root)
        self.buttom_frame.pack(fill=tk.BOTH)

        self.save_word_button = tk.Button(self.buttom_frame,**BUTTON_STYLE,text= "Save\nword")
        self.save_word_button.pack(side=tk.LEFT)

        self.used_words = tk.Label(self.buttom_frame,justify='l',text = "as ed",font=("Courier", 30),
                                       bg="lightgray", width=23, relief="ridge")
        self.used_words.pack(side=tk.LEFT,fill=tk.BOTH,expand='true')
#-------------------------------------------------#
    #timer
    def update_timer(self):
        remaining_time = self.end_time - time.time()
        if remaining_time > 0:
            minutes = int(remaining_time // 60)
            seconds = int(remaining_time % 60)
            self.timer_label.config(text="time: {:02d}:{:02d}".format(minutes, seconds))
            self.timer_label.after(1000, self.update_timer)
        else:
            self.timer_label.config(text="Time's up!")
    #run methos(incomplete)
    def run(self):
        self.end_time = time.time() + self.duration
        self.update_timer()
        self.root.mainloop()
        self.root.mainloop()

#---------------------------------buttons grid and button settings


    def create_buttons_in_lower_frame(self,table) -> None:
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
                button = tk.Button(self.button_grid_frame, text=table[row][col].upper(), **BUTTON_STYLE,command= lambda r=row,c=col: self._display_label.config(text=self.table[r][c]))
                button.grid(row=row, column=col, sticky=tk.NSEW)
                #make buttons shine if mouse on him
                self.change_button_color_on_hover(button,BUTTON_HOVER_COLOR,REGULAR_COLOR)
                #append button
                row_buttons.append(button)
            self.grid_buttons.append(row_buttons)


    #make button shine when mouse on him
    def change_button_color_on_hover(self,button, hover_color, regular_color):
        def on_enter(event):
            button.config(background=hover_color)

        def on_leave(event):
            button.config(background=regular_color)

        button.bind("<Enter>", on_enter)
        button.bind("<Leave>", on_leave)

    #button press when pressing button
    def _key_pressed(self, event: Any) -> None:
        if event.char in self._buttons:
            self._simulate_button_press(event.char)
        elif event.keysym == "Return":
            self._simulate_button_press("=")
    def _simulate_button_press(self, button_char: str) -> None:
        """make a button light up as if it is pressed,
        and then return to normal"""
        button = self._buttons[button_char]
        button["bg"] = BUTTON_ACTIVE_COLOR

        def return_button_to_normal() -> None:
            # find which widget the mouse is pointing at:
            x, y = self._main_window.winfo_pointerxy()
            widget_under_mouse = self._main_window.winfo_containing(x, y)
            # change color accordingly:
            if widget_under_mouse is button:
                button["bg"] = BUTTON_HOVER_COLOR
            else:
                button["bg"] = REGULAR_COLOR

        button.invoke()  # type: ignore
        button.after(100, func=return_button_to_normal)

        def reset():
            root = tk.Tk()
#--------------------------------------------------------

a = Game([
    [ "Ce", "D", "E", "F"],
    ["G", "H", "I", "J", "K", "L"],
    ["M", "N", "O", "P", "Q", "R"],
    ["C", "D", "E", "F"]

])
a.run()
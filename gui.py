import tkinter as tk
from boggle import Boggle

ROOT_NAME = "Boggle"
BUTTON_HOVER_COLOR = 'gray'
REGULAR_COLOR = 'lightgray'
BUTTON_ACTIVE_COLOR = 'slateblue'
BUTTON_STYLE = {"font": ("Courier", 30),
                "borderwidth": 1,
                "relief": tk.RAISED,
                "bg": REGULAR_COLOR,
                "activebackground": BUTTON_ACTIVE_COLOR}
ROWS = 4
COLS = 4


class Game:
    """The class get a Boggle API and make the game visible"""
    """And make the game able to be played by running the program"""

    def __init__(self, boggle: Boggle):  # basic init
        """Init of the display and get the API"""
        self.__boggle = boggle
        self.__current_word = ""
        self.__create_gui()

    # ---------------------------------create all formats
    # create all
    def __create_gui(self):
        """Summerize the create of the whole screen view"""
        self.__root = tk.Tk()
        self.__root.title(ROOT_NAME)
        self.__create_upper_frame()
        self.__create_display_label()
        self.__create_buttons_grid()
        self.__create_buttom_format()

    # Create a timer and score frame
    def __create_upper_frame(self):
        """Creates the upper frame(the place for the timer and the score)"""
        self.__upper_frame = tk.Frame(self.__root)
        self.__upper_frame.pack(pady=10, fill=tk.BOTH)
        self.__create_timer_label()
        self.__create_score_label()

    def __create_timer_label(self):
        """Creates the place for the timer"""
        self.__timer_label = tk.Label(self.__upper_frame, text="", font=("Helvetica", 24, "bold"), justify='right')
        self.__timer_label.pack(side=tk.RIGHT)

    def __create_score_label(self):
        """Creates the place for the score"""
        self.__score_label = tk.Label(self.__upper_frame,
                                      text="score: 0", font=("Helvetica", 24, "bold"), justify='left')
        self.__score_label.pack(side=tk.LEFT)

    def __create_display_label(self):  # create a label for current word
        """Creates the label to display the current word that the user creates"""
        self.__display_label = tk.Label(self.__root, font=("Courier", 30),
                                        bg="lightgray", width=23, relief="ridge")
        self.__display_label.pack(side=tk.TOP, fill=tk.BOTH)

    def __create_buttons_grid(self):  # create a frame for buttons
        """Creates the table of the game buttons that represent chars(and QU)"""
        self.__button_grid_frame = tk.Frame(self.__root)
        self.__button_grid_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        self.__create_buttons_in_lower_frame()

    def __create_buttom_format(self):
        """Creates the save word button, and the display of the used words"""
        self.__buttom_frame = tk.Frame(self.__root)
        self.__buttom_frame.pack(fill=tk.BOTH)
        self.__create_save_word_btn()
        self.__create_used_words_label()

    def __create_save_word_btn(self):
        """Creates the save word button"""
        self.__save_word_button = tk.Button(self.__buttom_frame, **BUTTON_STYLE,
                                            text="Save\nword", command=self.__save_word)
        self.__save_word_button.pack(side=tk.LEFT)

    def __create_used_words_label(self):
        """Creates the display of the used words"""
        self.__used_words = tk.Label(self.__buttom_frame, justify='left', text="", font=("Courier", 20), anchor='n',
                                     bg="lightgray", width=23, relief="ridge")
        self.__used_words.pack(side=tk.LEFT, fill=tk.BOTH, expand=1)

    def __save_word(self):
        """Click on the save word button"""
        self.__boggle.submit_word()
        self.__current_word = ""
        self.__update_current_word()
        self.__update_score()
        self.__update_used_words_screen()

    # ------------------------------------------------- screen updates

    def __update_timer(self):
        """Method to update the timer and screen the current time"""
        remaining_time = self.__boggle.get_current_time()
        if remaining_time > 0:
            minutes = int(remaining_time // 60)
            seconds = int(remaining_time % 60)
            self.__timer_label.config(text="time: {:02d}:{:02d}".format(minutes, seconds))
            self.__timer_label.after(1000, self.__update_timer)
        else:
            self.quit()

    def quit(self):
        """Destroys the screen"""
        self.__root.destroy()

    def on_closing(self):
        quit()

    def __update_score(self):
        """Updates the score display"""
        self.__score_label.config(text="score:{:2d}".format(self.__boggle.score))

    def __update_used_words_screen(self):
        """Updates the used words screen and limit them to 5 words in line"""
        string, counter = "", 0
        lst = self.__boggle.used_words
        for word in lst:
            if counter % 5 == 0:  # more than 5 words in line
                string += "\n"
            string += (word + " ")
            counter += 1
        self.__used_words.config(text=string)

    def __update_current_word(self):
        """Updates the current word display"""
        self.__display_label.config(text=self.__current_word)

    def run(self):
        """Run the whole game"""
        self.__update_timer()
        self.__root.mainloop()

    # ---------------------------------buttons grid and button settings
    def __create_buttons_in_lower_frame(self) -> None:
        """Summerizes the grid button building"""
        self.__create_grid_configure()
        self.__create_buttons_on_grid()

    def __create_grid_configure(self):
        """Create the figure of the grid table"""
        for i in range(COLS):
            tk.Grid.columnconfigure(self.__button_grid_frame, i, weight=1)  # type: ignore
        for i in range(ROWS):
            tk.Grid.rowconfigure(self.__button_grid_frame, i, weight=1)  # type: ignore

    def __create_buttons_on_grid(self):
        """Create the buttons on the grid"""
        for row in range(ROWS):
            for col in range(COLS):
                # create button and place in grid
                button = tk.Button(self.__button_grid_frame, text=self.__boggle.get_value_by_location(row, col).upper(),
                                   **BUTTON_STYLE, command=lambda r=row, c=col: self.__grid_button_click(r, c))
                button.grid(row=row, column=col, sticky=tk.NSEW)
                # make buttons shine if mouse on him
                self.__change_button_color_on_hover(button, BUTTON_HOVER_COLOR, REGULAR_COLOR)

    def __grid_button_click(self, x, y):
        """Grid button onclick, add the char to current word"""
        self.__boggle.add_to_current_path(x, y)
        self.__current_word += self.__boggle.get_value_by_location(x, y)
        self.__update_current_word()

    def __change_button_color_on_hover(self, button, hover_color, regular_color):
        """Make button shine when mouse on him"""
        def __on_enter(event):
            button.config(background=hover_color)

        def __on_leave(event):
            button.config(background=regular_color)

        button.bind("<Enter>", __on_enter)
        button.bind("<Leave>", __on_leave)


# --------------------------------------------------------

if __name__ == '__main__':
    b = Boggle()
    b.start_game()
    a = Game(b)
    a.run()

from typing import Dict, List, Callable, Any
import tkinter as tk
import time
BUTTON_HOVER_COLOR = 'gray'
REGULAR_COLOR = 'lightgray'
BUTTON_ACTIVE_COLOR = 'slateblue'

BUTTON_STYLE = {"font": ("Courier", 30),
                "borderwidth": 1,
                "relief": tk.RAISED,
                "bg": REGULAR_COLOR,
                "activebackground": BUTTON_ACTIVE_COLOR}
class Game:
    buttons: Dict[str, tk.Button] = {}
    def __init__(self,table):
        self.duration = 180  # 3 minutes (in seconds)

        self.root = tk.Tk()
        self.root.title("Boogle")

        # Create a timer frame for the timer
        self.upper_frame = tk.Frame(self.root)
        self.upper_frame.pack(pady=10)

        self.timer_label = tk.Label(self.upper_frame, text="03:00", font=("Helvetica", 24, "bold"))
        self.timer_label.pack(side=tk.LEFT,padx=100)

        self.score_label = tk.Label(self.upper_frame, text="score: 0", font=("Helvetica", 24, "bold"))
        self.score_label.pack(side=tk.RIGHT,padx=100)


        # create a label for word
        self._display_label = tk.Label(self.root, font=("Courier", 30),
                                        bg="lightgray", width=23, relief="ridge")
        self._display_label.pack(side=tk.TOP, fill=tk.BOTH)

        # create a frame for buttons
        self._lower_frame = tk.Frame(self.root)
        self._lower_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        self.create_buttons_in_lower_frame(table)
        self.root.bind("<Key>", self._key_pressed)

    def update_timer(self):
        remaining_time = self.end_time - time.time()
        if remaining_time > 0:
            minutes = int(remaining_time // 60)
            seconds = int(remaining_time % 60)
            self.timer_label.config(text="{:02d}:{:02d}".format(minutes, seconds))
            self.timer_label.after(1000, self.update_timer)
        else:
            self.timer_label.config(text="Time's up!")
    #def update_score(self,pts):

    def run(self):
        self.end_time = time.time() + self.duration
        self.update_timer()
        self.root.mainloop()
        self.root.mainloop()
    def set_display(self, display_text: str) -> None:
        self._display_label["text"] = display_text

    def set_button_command(self, button_name: str, cmd: Callable[[], None]) -> None:
        self._buttons[button_name].configure(command=cmd)

    def get_button_chars(self) -> List[str]:
        return list(self._buttons.keys())

    def create_buttons_in_lower_frame(self,table) -> None:
        for i in range(len(table[0])):
            tk.Grid.columnconfigure(self._lower_frame, i, weight=1)  # type: ignore

        for i in range(len(table)):
            tk.Grid.rowconfigure(self._lower_frame, i, weight=1)  # type: ignore

        for x in range(len(table)):
            for y in range(len(table[0])):
                self._make_button(table[x][y],x,y)

    def _make_button(self, button_char: str, row: int, col: int,
                     rowspan: int = 1, columnspan: int = 1) -> tk.Button:
        button = tk.Button(self._lower_frame, text=button_char, **BUTTON_STYLE)
        button.grid(row=row, column=col, rowspan=rowspan, columnspan=columnspan, sticky=tk.NSEW)
        self.buttons[button_char] = button

        def _on_enter(event: Any) -> None:
            button['background'] = BUTTON_HOVER_COLOR

        def _on_leave(event: Any) -> None:
            button['background'] = REGULAR_COLOR

        button.bind("<Enter>", _on_enter)
        button.bind("<Leave>", _on_leave)
        return button

    def _key_pressed(self, event: Any) -> None:
        """the callback method for when a key is pressed.
        It'll simulate a button press on the right button."""
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


a = Game([
    [ "C", "D", "E", "F"],
    ["G", "H", "I", "J", "K", "L"],
    ["M", "N", "O", "P", "Q", "R"],

])
a.run()
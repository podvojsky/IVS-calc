#!/usr/bin/env python3

"""@package calc_view
This module implements graphical user interface
for the calculator using tkinter module.
"""

import sys
import tkinter as tk
import colors as c


class Calculator:
    """_summary_
    """
    ICON_PATH = "./icons/calculator-96.png"
    FONT = "Ubuntu Mono"

    def __init__(self) -> None:
        """Initializes a new Calculator object.
        """
        self.root = tk.Tk()
        self.cfg_window()
        self.create_display()
        self.create_buttons()
        
        
    @staticmethod
    def eprint(e: object) -> None:
        """Static method for printing errors to standard error output.

        Args:
            e (object): Any type of exception.
        """
        print(e, file=sys.stderr)


    def start(self) -> None:
        """Runs the Calculator.
        """
        self.root.mainloop()
        
    def cfg_window(self) -> None:
        """Configures Calculator window parameters.
        
        This method configures icon, size, title
        and other attributes for main Calculator window.
        """
        
        # Setting window icon.
        try:
            icon = tk.PhotoImage(file=Calculator.ICON_PATH)
            self.root.wm_iconphoto(False, icon)
        except tk.TclError as icon_not_found:
            self.eprint(icon_not_found)
            
        self.root.title("Calculator")
        self.root.geometry("350x450")
        self.root.resizable(width=False, height=False)
        self.root["padx"] = 20
        self.root["pady"] = 20
        self.root.configure(bg=c.WINDOW_BG)
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        self.root.rowconfigure(1, weight=4)
        
    def create_display(self) -> None:
        """Creates output display.
        """
        self.display_frame = tk.Frame(self.root, bg=c.WINDOW_BG, width=300)
        self.display_frame.grid(row=0, column=0)
        
        self.display = tk.Entry(self.display_frame, bg=c.DISPLAY_BG, fg=c.DISPLAY_FG, width=300, font=(Calculator.FONT, 30), justify="right")
        
        self.display.insert(index=0, string="abc ")
        self.display.insert(index="end", string=u'123')
        self.display.configure(state="readonly")
        
        self.display.pack()
        


if __name__ == "__main__":
    calculator = Calculator()
    calculator.start()

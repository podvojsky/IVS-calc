#!/usr/bin/env python3

"""@package calc_view
This module implements graphical user interface
for the calculator using tkinter module.
"""

import sys
import tkinter as tk


class Calculator:
    """_summary_
    """
    icon_path = "./icons/calculator-96.png"

    def __init__(self) -> None:
        """Initializes a new Calculator object.
        """
        self.root = tk.Tk()
        self.cfg_window()
        
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
        
        """Setting window icon."""
        try:
            icon = tk.PhotoImage(file=Calculator.icon_path)
            self.root.wm_iconphoto(False, icon)
        except tk.TclError as icon_not_found:
            self.eprint(icon_not_found)
            
        self.root.title("Calculator")
        self.root.geometry("350x450")
        self.root.resizable(width=False, height=False)


if __name__ == "__main__":
    calculator = Calculator()
    calculator.start()

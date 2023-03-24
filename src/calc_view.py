#!/usr/bin/env python3

"""@package calc_view
This module implements graphical user interface
for the calculator using tkinter module.
"""

import tkinter as tk


class Calculator:
    """_summary_
    """

    def __init__(self) -> None:
        """_summary_
        """
        self.root = tk.Tk()
        self.root.title("Calculator")
        self.root.minsize(350, 450)

    def start(self) -> None:
        """_summary_
        """
        self.root.mainloop()


if __name__ == "__main__":
    calculator = Calculator()
    calculator.start()

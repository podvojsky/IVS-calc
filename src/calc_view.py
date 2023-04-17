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
        self.style_buttons()
        
        
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
        self.root.rowconfigure(1, weight=1)
        
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
        
    def create_buttons(self) -> None:
        """Creates buttons for numbers and functions.
        """
        
        def create_button(btn_label: str, grid_position: tuple[int, int]):
            button = tk.Button(self.buttons_frame, text=btn_label, font=(Calculator.FONT, 20), width=2, bg=c.NUMBER_BTN_BG, fg=c.NUMBER_BTN_FG)
            button.grid(row=grid_position[0], column=grid_position[1], padx=2, pady=2)
            self.buttons[btn_label] = button
            pass
        
        
        self.buttons_frame = tk.Frame(self.root, bg=c.WINDOW_BG, width=300)
        self.buttons_frame.grid(row=1, column=0)
        
        self.buttons = {}
        
        buttons_template = [
            "C", "x^y", "y√x", "ln", "!",
            "7", "8", "9", "÷", "√x",
            "4", "5", "6", "*", "x^2",
            "1", "2", "3", "-", "=",
            "+/-", "0", ".", "+"
        ]
        
        for i, btn_label in enumerate(buttons_template):
            create_button(btn_label, (i // 5, i % 5))
            
        self.buttons["="].grid(rowspan=2)
        self.buttons["="].config(height=2, pady=13)
        
        print(self.buttons)
        
        pass
    
    def style_buttons(self):
        self.buttons["="].configure(bg=c.EQ_BTN_BG, fg=c.EQ_BTN_FG)
        function_buttons = ["C", "x^y", "y√x", "ln", "!", "√x", "x^2"]
        operator_buttons = ["+", "-", "*", "÷", ".", "+/-"]
        for fn_btn in function_buttons:
            self.buttons[fn_btn].configure(bg=c.FUNCTION_BTN_BG, fg=c.FUNCTION_BTN_FG)
        for oper_btn in operator_buttons:
            self.buttons[oper_btn].configure(bg=c.OPERATOR_BTN_BG, fg=c.OPERATOR_BTN_FG)
        pass
        


if __name__ == "__main__":
    calculator = Calculator()
    calculator.start()

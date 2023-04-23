#!/usr/bin/env python3

"""@package calc_view
This module implements graphical user interface
for the calculator using tkinter module.
"""

import sys
import tkinter as tk
import src.colors as c
import src.math_lib as mth
from math import e as en


class Calculator:
    """_summary_
    """
    ICON_PATH = "/usr/share/icons/hicolor/96x96/apps/ivscalc-96.png"
    FONT = "Ubuntu Mono"
    
    clean_display = False
    last_operator = ""
    function_buttons = ["C", "x^y", "y√x", "ln", "!", "√x", "x^2"]
    operator_buttons = ["+", "-", "*", "÷", ".", "+/-"]

    def __init__(self) -> None:
        """Initializes a new Calculator object.
        """
        self.root = tk.Tk()
        self.cfg_window()
        self.create_display()
        self.create_buttons()
        self.style_buttons()
        self.add_button_funct()
        
        
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
        
        for fn_btn in __class__.function_buttons:
            self.buttons[fn_btn].configure(bg=c.FUNCTION_BTN_BG, fg=c.FUNCTION_BTN_FG)
        for oper_btn in __class__.operator_buttons:
            self.buttons[oper_btn].configure(bg=c.OPERATOR_BTN_BG, fg=c.OPERATOR_BTN_FG)
        pass
    
    def add_button_funct(self):
        for button in self.buttons.values():
            button.config(command=lambda text=button.cget("text"): self.button_onclick(text))
        
    def button_onclick(self, inpt):
        self.display.configure(state="normal")
        
        match inpt:
            case "C":
                self.display.delete(0, tk.END)
            case "=":
                try:
                    eq = self.display.get()
                    eq_split = eq.split(__class__.last_operator)
                    eq_operands = (float(eq_split[0]), float(eq_split[1]))
                    print(eq_split)
                    match __class__.last_operator:
                        case "+":
                            result = mth.add(eq_operands[0], eq_operands[1])
                            pass
                        case "-":
                            result = mth.sub(eq_operands[0], eq_operands[1])
                            pass
                        case "*":
                            result = mth.mul(eq_operands[0], eq_operands[1])
                            pass
                        case "÷":
                            result = mth.div(eq_operands[0], eq_operands[1])
                            pass
                        case "^":
                            result = mth.pow(eq_operands[0], eq_operands[1])
                            pass
                        case "^2":
                            result = mth.pow(eq_operands[0], 2)
                            pass
                        case "√":
                            result = mth.sqrt(eq_operands[0], eq_operands[1])
                            pass
                    if result.is_integer():
                        result = int(result)
                    # formatted_result = '{:,}'.format(result)
                    # print(formatted_result)
                    self.display.delete(0, tk.END)
                    self.display.insert(tk.END, str(result))
                except IndexError:
                    self.display.delete(0, tk.END)
                    self.display.insert(tk.END, "Zadejte číslo!")
                    __class__.clean_display = True
                except ValueError:
                    pass
                    
            case "+":
                operand1 = self.display.get()
                try:
                    operand1_int = float(operand1)
                except ValueError:
                    self.display.delete(0, tk.END)
                    if (operand1 == ""):
                        self.display.insert(tk.END, "Zadejte číslo!")
                    elif ("+" in __class__.operator_buttons[:-2]):
                        self.display.insert(tk.END, "Pouze dva oper.")
                    else:
                        self.display.insert(tk.END, "Zadejte číslo!")
                    __class__.clean_display = True
                    return
                self.display.insert(tk.END, inpt)
                __class__.last_operator = "+"
                pass
            case "-":
                operand1 = self.display.get()
                try:
                    operand1_int = float(operand1)
                except ValueError:
                    self.display.delete(0, tk.END)
                    if (operand1 == ""):
                        self.display.insert(tk.END, "Zadejte číslo!")
                    elif ("-" in __class__.operator_buttons[:-2]):
                        self.display.insert(tk.END, "Pouze dva oper.")
                    else:
                        self.display.insert(tk.END, "Zadejte číslo!")
                    __class__.clean_display = True
                    return
                self.display.insert(tk.END, inpt)
                __class__.last_operator = "-"
                pass
            case "*":
                operand1 = self.display.get()
                try:
                    operand1_int = float(operand1)
                except ValueError:
                    self.display.delete(0, tk.END)
                    if (operand1 == ""):
                        self.display.insert(tk.END, "Zadejte číslo!")
                    elif ("*" in __class__.operator_buttons[:-2]):
                        self.display.insert(tk.END, "Pouze dva oper.")
                    else:
                        self.display.insert(tk.END, "Zadejte číslo!")
                    __class__.clean_display = True
                    return
                self.display.insert(tk.END, inpt)
                __class__.last_operator = "*"
                pass
            case "÷":
                operand1 = self.display.get()
                try:
                    operand1_int = float(operand1)
                except ValueError:
                    self.display.delete(0, tk.END)
                    if (operand1 == ""):
                        self.display.insert(tk.END, "Zadejte číslo!")
                    elif ("÷" in __class__.operator_buttons[:-2]):
                        self.display.insert(tk.END, "Pouze dva oper.")
                    else:
                        self.display.insert(tk.END, "Zadejte číslo!")
                    __class__.clean_display = True
                    return
                self.display.insert(tk.END, inpt)
                __class__.last_operator = "÷"
                pass
            case "x^y":
                operand1 = self.display.get()
                try:
                    operand1_int = float(operand1)
                except ValueError:
                    self.display.delete(0, tk.END)
                    if (operand1 == ""):
                        self.display.insert(tk.END, "Zadejte číslo!")
                    elif ("÷" in __class__.operator_buttons[:-2]):
                        self.display.insert(tk.END, "Pouze dva oper.")
                    else:
                        self.display.insert(tk.END, "Zadejte číslo!")
                    __class__.clean_display = True
                    return
                self.display.insert(tk.END, "^")
                __class__.last_operator = "^"
                pass
            case "y√x":
                operand1 = self.display.get()
                try:
                    operand1_int = float(operand1)
                except ValueError:
                    self.display.delete(0, tk.END)
                    if (operand1 == ""):
                        self.display.insert(tk.END, "Zadejte číslo!")
                    elif ("÷" in __class__.operator_buttons[:-2]):
                        self.display.insert(tk.END, "Pouze dva oper.")
                    else:
                        self.display.insert(tk.END, "Zadejte číslo!")
                    __class__.clean_display = True
                    return
                self.display.insert(tk.END, "√")
                __class__.last_operator = "√"
                pass
            
            
            
            case "+/-":
                operand1 = self.display.get()
                try:
                    operand1_int = float(operand1)
                except ValueError:
                    self.display.delete(0, tk.END)
                    self.display.insert(tk.END, "Zadejte číslo!")
                    __class__.clean_display = True
                    return
                operand1_int = operand1_int * (-1)
                self.display.delete(0, tk.END)
                if operand1_int.is_integer():
                    operand1_int = int(operand1_int)
                self.display.insert(tk.END, str(operand1_int))
                pass
            case "x^2":
                operand1 = self.display.get()
                try:
                    operand1_int = float(operand1)
                except ValueError:
                    self.display.delete(0, tk.END)
                    self.display.insert(tk.END, "Zadejte číslo!")
                    __class__.clean_display = True
                    return
                result = mth.pow(operand1_int, 2)
                self.display.delete(0, tk.END)
                if result.is_integer():
                    result = int(result)
                self.display.insert(tk.END, str(result))
                pass
            case "ln":
                operand1 = self.display.get()
                try:
                    operand1_int = float(operand1)
                except ValueError:
                    self.display.delete(0, tk.END)
                    self.display.insert(tk.END, "Zadejte číslo!")
                    __class__.clean_display = True
                    return
                result = mth.log(operand1_int, en)
                self.display.delete(0, tk.END)
                if result.is_integer():
                    result = int(result)
                self.display.insert(tk.END, str(result))
            case "!":
                operand1 = self.display.get()
                try:
                    operand1_int = float(operand1)
                except ValueError:
                    self.display.delete(0, tk.END)
                    self.display.insert(tk.END, "Zadejte číslo!")
                    __class__.clean_display = True
                    return
                result = mth.fac(operand1_int)
                self.display.delete(0, tk.END)
                if result.is_integer():
                    result = int(result)
                self.display.insert(tk.END, str(result))
            case "√x":
                operand1 = self.display.get()
                try:
                    operand1_int = float(operand1)
                except ValueError:
                    self.display.delete(0, tk.END)
                    self.display.insert(tk.END, "Zadejte číslo!")
                    __class__.clean_display = True
                    return
                result = mth.sqrt(2, operand1_int)
                self.display.delete(0, tk.END)
                if result.is_integer():
                    result = int(result)
                self.display.insert(tk.END, str(result))
            
            case _:
                if __class__.clean_display:
                    self.display.delete(0, tk.END)
                    __class__.clean_display = False
                self.display.insert(tk.END, inpt)
            
        self.display.configure(state="readonly")


def main():
    calculator = Calculator()
    calculator.start()

if __name__ == "__main__":
    main()

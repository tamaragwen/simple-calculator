#!/usr/bin/env python3
"""
Simple GUI Calculator using tkinter
"""

import tkinter as tk
from tkinter import ttk
import operator


class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Python GUI Calculator")
        self.root.geometry("300x400")
        self.root.resizable(False, False)
        
        # Variables
        self.current = "0"
        self.previous = None
        self.operation = None
        self.new_number = True
        
        # Create GUI
        self.create_widgets()
        
    def create_widgets(self):
        # Display
        self.display_var = tk.StringVar(value="0")
        display = tk.Entry(
            self.root, 
            textvariable=self.display_var, 
            font=("Arial", 20),
            justify="right",
            state="readonly",
            width=15
        )
        display.grid(row=0, column=0, columnspan=4, padx=5, pady=5, sticky="ew")
        
        # Button layout
        buttons = [
            ("C", 1, 0), ("±", 1, 1), ("%", 1, 2), ("÷", 1, 3),
            ("7", 2, 0), ("8", 2, 1), ("9", 2, 2), ("×", 2, 3),
            ("4", 3, 0), ("5", 3, 1), ("6", 3, 2), ("−", 3, 3),
            ("1", 4, 0), ("2", 4, 1), ("3", 4, 2), ("+", 4, 3),
            ("0", 5, 0), (".", 5, 2), ("=", 5, 3)
        ]
        
        # Create buttons
        for (text, row, col) in buttons:
            if text == "0":
                # Make 0 button span two columns
                btn = tk.Button(
                    self.root,
                    text=text,
                    font=("Arial", 16),
                    command=lambda t=text: self.button_click(t),
                    height=2,
                    width=10
                )
                btn.grid(row=row, column=col, columnspan=2, padx=2, pady=2, sticky="ew")
            else:
                btn = tk.Button(
                    self.root,
                    text=text,
                    font=("Arial", 16),
                    command=lambda t=text: self.button_click(t),
                    height=2,
                    width=5
                )
                btn.grid(row=row, column=col, padx=2, pady=2, sticky="ew")
                
        # Configure grid weights
        for i in range(4):
            self.root.columnconfigure(i, weight=1)
            
    def button_click(self, value):
        if value.isdigit() or value == ".":
            self.number_input(value)
        elif value == "C":
            self.clear()
        elif value == "±":
            self.toggle_sign()
        elif value == "%":
            self.percentage()
        elif value == "=":
            self.calculate()
        elif value in ["÷", "×", "−", "+"]:
            self.set_operation(value)
            
    def number_input(self, digit):
        if self.new_number:
            self.current = digit if digit != "." else "0."
            self.new_number = False
        else:
            if digit == "." and "." in self.current:
                return  # Prevent multiple decimal points
            self.current += digit
        
        self.display_var.set(self.current)
        
    def clear(self):
        self.current = "0"
        self.previous = None
        self.operation = None
        self.new_number = True
        self.display_var.set("0")
        
    def toggle_sign(self):
        if self.current != "0":
            if self.current.startswith("-"):
                self.current = self.current[1:]
            else:
                self.current = "-" + self.current
            self.display_var.set(self.current)
            
    def percentage(self):
        try:
            result = float(self.current) / 100
            self.current = str(result)
            self.display_var.set(self.current)
            self.new_number = True
        except ValueError:
            self.display_var.set("Error")
            
    def set_operation(self, op):
        if not self.new_number and self.operation:
            # Perform pending calculation
            self.calculate()
            
        self.previous = self.current
        self.operation = op
        self.new_number = True
        
    def calculate(self):
        if self.previous is None or self.operation is None:
            return
            
        try:
            prev = float(self.previous)
            curr = float(self.current)
            
            operations = {
                "+": operator.add,
                "−": operator.sub,
                "×": operator.mul,
                "÷": operator.truediv
            }
            
            if self.operation == "÷" and curr == 0:
                self.display_var.set("Error")
                self.clear()
                return
                
            result = operations[self.operation](prev, curr)
            
            # Format result
            if result.is_integer():
                self.current = str(int(result))
            else:
                self.current = str(round(result, 10))
                
            self.display_var.set(self.current)
            self.previous = None
            self.operation = None
            self.new_number = True
            
        except (ValueError, ZeroDivisionError, KeyError):
            self.display_var.set("Error")
            self.clear()


def main():
    root = tk.Tk()
    calculator = Calculator(root)
    root.mainloop()


if __name__ == "__main__":
    main()
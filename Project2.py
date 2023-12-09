import tkinter as tk
from tkinter import ttk
import math


class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")

        self.result_var = tk.StringVar()
        self.create_gui()

    def create_gui(self):
        # Entry widget to display the result
        entry_style = ttk.Style()
        entry_style.configure("Entry.TEntry", background="#BCE6B0", font=('Arial', 18))
        entry = ttk.Entry(self.root, textvariable=self.result_var, style="Entry.TEntry", justify='right')
        entry.grid(row=0, column=0, columnspan=6, sticky='nsew')

        # Buttons
        button_style = ttk.Style()
        button_style.configure("TButton", font=('Arial', 14))
        button_style.map("TButton", background=[("active", "#FFD1DC"), ("!active", "#FFD1DC")])

        buttons = [
            'π', '√', 'sin', 'cos',
            'tan', 'log', '(', ')',
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+',
            'Clear'
        ]

        # Add buttons to the GUI
        row_val, col_val = 1, 0
        for button_text in buttons:
            column_span = 2 if button_text == 'Clear' else 1  # Set column span to 2 for 'Clear' button
            ttk.Button(self.root, text=button_text, command=lambda btn=button_text: self.on_button_click(btn), width=6,
                       style="TButton"
                       ).grid(row=row_val, column=col_val, sticky='nsew', columnspan=column_span)
            col_val += column_span
            if col_val > 4:
                col_val = 0
                row_val += 1

        # Configure row and column weights to make the GUI expandable
        for i in range(5):
            self.root.grid_rowconfigure(i, weight=1)
            self.root.grid_columnconfigure(i, weight=1)

    def on_button_click(self, button_text):
        current_input = self.result_var.get()

        if button_text == 'Clear':
            self.result_var.set('')
        elif button_text == '=':
            try:
                result = eval(current_input)
                self.result_var.set(result)
            except Exception:
                self.result_var.set('Error')
        elif button_text == 'π':
            self.result_var.set(current_input + str(math.pi))
        elif button_text == '√':
            self.result_var.set(current_input + 'sqrt(')
        elif button_text == '(':
            self.result_var.set(current_input + '(')
        elif button_text == ')':
            # Count the number of open and close parentheses
            open_count = current_input.count('(')
            close_count = current_input.count(')')

            # Add a close parenthesis only if there are open parentheses to balance
            if open_count > close_count:
                self.result_var.set(current_input + ')')
        elif button_text in ['sin', 'cos', 'tan', 'log']:
            self.result_var.set(current_input + button_text + '(')
        else:
            self.result_var.set(current_input + button_text)


def main():
    root = tk.Tk()
    root.geometry("400x500")  # Set the initial size of the window
    app = Calculator(root)
    root.mainloop()


if __name__ == "__main__":
    main()

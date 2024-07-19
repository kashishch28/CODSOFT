import tkinter as tk
from tkinter import messagebox

class Calculator:
    def __init__(self, master):
        self.master = master
        master.title("Calculator")
        master.geometry("420x450")
        master.configure(background="black")

        # Create entry field
        self.entry_field = tk.Entry(master, width=25, font=("Arial", 20), relief="ridge", borderwidth=10)
        self.entry_field.grid(row=0, column=0, columnspan=4, padx=5, pady=5)

        #Number buttons
        buttons = ['7', '8', '9', '/','4', '5', '6', '*','1', '2', '3', '-','0', '.', '=', '+']
        row_val = 1
        col_val = 0
        for button in buttons:
            tk.Button(master, text=button, width=5, font=("Arial", 12), relief="ridge", borderwidth=2, command=lambda button=button: self.click_button(button), bg="grey", fg="white").grid(row=row_val, column=col_val, padx=5, pady=5)
            col_val += 1
            if col_val > 3:
                col_val = 0
                row_val += 1

        #Clear button
        tk.Button(master, text="Clear", width=10, font=("Arial", 12), relief="ridge", borderwidth=2, command=self.clear, bg="#FF69B4", fg="white").grid(row=row_val, column=0, columnspan=4, padx=5, pady=5)

    def click_button(self, button):
        if button == '=':
            try:
                result = eval(self.entry_field.get())
                self.entry_field.delete(0, tk.END)
                self.entry_field.insert(tk.END, result)
            except Exception as e:
                self.entry_field.delete(0, tk.END)
                self.entry_field.insert(tk.END, "Error")
        else:
            self.entry_field.insert(tk.END, button)

    def clear(self):
        self.entry_field.delete(0, tk.END)

root = tk.Tk()
my_calculator = Calculator(root)


root.mainloop()
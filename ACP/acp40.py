import tkinter as tk
from tkinter import messagebox

def convert():
        inches = float(einches.get())
        cm = inches * 2.54
        label_result.config(text=f"{cm:.2f} cm")
    
root = tk.Tk()
root.title("Inches to cm Converter")
label_inches = tk.Label(root, text="Inches:")
label_inches.grid(row=0, column=0, padx=10, pady=10)
einches = tk.Entry(root)
einches.grid(row=0, column=1, padx=10, pady=10)
button_convert = tk.Button(root, text="Convert", command=convert)
button_convert.grid(row=1, column=0, columnspan=2, pady=10)
label_result = tk.Label(root, text="Result: ")
label_result.grid(row=2, column=0, columnspan=2, pady=10)
root.mainloop()
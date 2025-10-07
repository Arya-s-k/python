import tkinter as tk

def calculate():
    num1 = float(e1.get())
    num2 = float(e2.get())
    result_label.config(text="Product: " + str(num1 * num2))

root = tk.Tk()
root.title("Product Calculator")

tk.Label(root, text="Number 1:").grid(row=0, column=0, padx=10, pady=5)
tk.Label(root, text="Number 2:").grid(row=1, column=0, padx=10, pady=5)

e1 = tk.Entry(root)
e2 = tk.Entry(root)
e1.grid(row=0, column=1, padx=10, pady=5)
e2.grid(row=1, column=1, padx=10, pady=5)

tk.Button(root, text="Calculate", command=calculate).grid(row=2, column=0, columnspan=2, pady=10)

result_label = tk.Label(root, text="Product: ")
result_label.grid(row=3, column=0, columnspan=2, pady=5)

root.mainloop()

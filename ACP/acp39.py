import tkinter as tk
from datetime import date

root = tk.Tk()
root.title("Age Calculator")

date_var = tk.StringVar()
month_var = tk.StringVar()
year_var = tk.StringVar()

def calculate_age():
    try:
        d = int(date_var.get())
        m = int(month_var.get())
        y = int(year_var.get())
        dt = date(y, m, d)

        today = date.today()

        age_in_years = today.year - dt.year
        
        if (today.month < dt.month) or \
           (today.month == dt.month and today.day < dt.day):
            age_in_years -= 1

        age = str(age_in_years)
        
        greeting = "Your age is " + age + " years old."

        text1.delete("1.0", tk.END)
        text1.insert("1.0", greeting)
    except Exception as e:
        text1.delete("1.0", tk.END)
        text1.insert("1.0", f"Invalid input: {e}")

frame1 = tk.Frame(root)
frame1.pack(padx=10, pady=10)

label1 = tk.Label(frame1, text="Date of Birth (D/M/Y):", bg='blue', fg='white')
label1.grid(row=0, column=0, columnspan=3, pady=5)

entry1 = tk.Entry(frame1, textvariable=date_var, width=5)
entry1.grid(row=1, column=0, padx=5)
tk.Label(frame1, text="Day").grid(row=2, column=0)

entry2 = tk.Entry(frame1, textvariable=month_var, width=5)
entry2.grid(row=1, column=1, padx=5)
tk.Label(frame1, text="Month").grid(row=2, column=1)

entry3 = tk.Entry(frame1, textvariable=year_var, width=7)
entry3.grid(row=1, column=2, padx=5)
tk.Label(frame1, text="Year").grid(row=2, column=2)

calculate_button = tk.Button(root, text="Calculate Age", command=calculate_age)
calculate_button.pack(pady=10)

text1 = tk.Text(root, height=3, width=40)
text1.pack(padx=10, pady=10)

root.mainloop()
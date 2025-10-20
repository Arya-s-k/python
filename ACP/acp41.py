from tkinter import *
from tkinter import messagebox

window = Tk()
window.title("Interest calculator")
window.geometry("400x400")

def si():
        p = float(entry1.get())
        n = float(entry3.get()) 
        r = float(entry2.get()) 
        i = (p * n * r) / 100
        messagebox.showinfo("Simple Interest", f"The Simple Interest is: ")
    


label1 = Label(window, text="Interest Calculator") 
label2 = Label(window, text="Principal (P)")
label3 = Label(window, text="Rate of Interest (R)")
label4 = Label(window, text="No of years (N)")

entry1 = Entry(window)
entry2 = Entry(window)
entry3 = Entry(window)

button1 = Button(window, text="Calculate Simple Interest", command=si) 

label1.place(x=100, y=20)
label2.place(x=50, y=100)
label3.place(x=50, y=150)
label4.place(x=50, y=200)
entry1.place(x=200, y=100)
entry2.place(x=200, y=150)
entry3.place(x=200, y=200)
button1.place(x=100, y=250)

window.mainloop()
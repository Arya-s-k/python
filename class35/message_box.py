from tkinter import * 
from tkinter import messagebox

tk = Tk() 
tk.geometry("400x400") 
tk.title("message box")
tk.configure(bg="blue")

def msg():
    messagebox.showwarning("alert!,virus found")
    

Button1 = Button(tk,text = "scan for virus",bg = "red", fg ="teal" , command=msg)
Button1.place(x= 150,y = 150)

tk.mainloop()
from tkinter import *
from datetime import date,datetime


root = Tk()
root.title("tkinter window")
root.geometry("500x500")
root.configure(bg = "white")

def greet():
    name = entry1.get()
    now = datetime.now()
    msg = "welcome to tkinter " + name + "\n todays date " + str(now)
    text1.delete('0.0','end')
    text1.insert(END,msg)
    

labell = Label(root,text = "Enter your name",bg = "red",fg = "navy")
labell.pack(pady=10)
entry1 = Entry()
Button1 = Button(root,text = "click",bg = "light green", fg = "cyan",command =greet)
entry1.pack(pady=10)
Button1.pack(pady=10)
text1 = Text(root,bg = "beige", width = 350, height = 10)
text1.pack(pady=10)


root.mainloop()
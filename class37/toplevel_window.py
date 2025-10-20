from tkinter import *

root = Tk()
root.geometry('300x300')

def win():
    top = Toplevel()
    top.geometry('150x100')
    top.configure(bg='teal')
    label2 = Label(top, text='the toplevel window')
    label2.pack()

label = Label(root, text="This is the top level window")
root.geometry('300x300')
label.pack()

Button1 = Button(root,text="click here",command=win)
Button1.pack()

root.mainloop()
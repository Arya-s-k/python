from tkinter import *
from os import system
system("pip install pillow")
from PIL import Image, ImageTk
from tkinter import messagebox
root = Tk()
root.title("Denomination Calculator")
root.geometry('600x600')
upload = Image.open("cash.jpg")
upload = upload.resize((300, 300))
img = ImageTk.PhotoImage(upload)

Labell = Label(root,image=img)
Labell.place(x=100,y=20)

Labell2 = Label(root,text="hey user ! welcome to denomination calculator app")
Labell2.place(y=20,x=320)

def msg():
    msgbox = messagebox.showinfo("alert","do you want to calculate denominate amount")
    if msgbox == "ok":
        topwin()
Button1 = Button(root,text="lets get started!",command=msg,bg="brown",fg="white")
Button1.place(x=180,y=370)

def topwin():
    def calculator():
        global amount
        amount = int(entry1.get())
        note2000 = amount//2000 
        amount = amount%2000
        note500 = amount//500
        amount = amount%500
        note100 = amount//100
        amount = amount%100
        t1.insert(END,str(2000))
        t2.insert(END,str(500))
        t3.insert(END,str(100))
    top = Toplevel()
    top.title("top level")
    top.geometry("400x400")
    label = Label(top,text = "enter amount")
    label.place(x=80,y=100)
    entry1 = Entry(top)
    entry1.place(x=180,y=100)
    lb1 = Label(top,text = "here are the number of notes for each")
    lb1.place(x=150,y=50)
    l1 = Label(top,text = "2000")
    l2 = Label(top,text = "500")
    l3 = Label(top,text = "100")
    t1 = Entry(top)
    t2 = Entry(top)
    t3 = Entry(top)
    btn = Button(top,text="calculate",command=calculator)
    entry1.place(x=180,y=100)
    btn.place(x=150,y=120)
    l1.place(x=100,y=200)
    l2.place(x=100,y=230)
    l3.place(x=100,y=250)
    t1.place(x=200,y=200)
    t2.place(x=200,y=230)
    t3.place(x=200,y=250)
    

root.mainloop()

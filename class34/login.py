from tkinter import *

window = Tk()
window.title("Number pad")
window.geometry("500x500")
window.configure(bg='grey')

def login():
    name = entry1.get()
    password = entry2.get()
    msg = "you have succefully logged in" + name
    text1.delete("1.0","end")
    text1.insert("1.0",msg)
    

frame1 = Frame(window, width=400, height=200, bg='skyblue', relief='groove')
frame1.place(x=50, y=20)

label1 = Label(window, text="Name", bg='skyblue', fg='navy', font=('Times', 14, 'bold'))
label1.place(x=80, y=40)
label1 = Label(window, text="login", bg='skyblue', fg='navy', font=('Times', 14, 'bold'))
label1.place(x=80, y=80)

entry1 = Entry()
entry1.place(x=180, y=40)
entry2 = Entry()
entry2.place(x=180, y=80)
entry2.config(show="*")

button1 = Button(window, text="Password", bg='Navy', fg='lightblue', font=('Times', 14, 'bold'),command=login)
button1.place(x=110, y=140)

text1 = Text(window, bg='gray', fg='white', font=('Times', 14, 'bold'), width=80, height=10)
text1.place(x=40, y=240)

window.mainloop()
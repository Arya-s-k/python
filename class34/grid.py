from tkinter import *
window = Tk()
window.title("number pad")
window.geometry('200x300')
window.configure(bg = "black")
n =[[9,8,7],[6,5,4],[3,2,1],[0,"#","*"]]

for i in range(4):
    window.rowconfigure(i,weight=0,minsize=70)
    for j in range(3):
        window.columnconfigure(j,weight=0,minsize=60)
        labell = Label(window,text=n[i][j],bg = "black",fg = "red",relief=RAISED)
        labell.grid(row = i,column = j )
        
window.mainloop()
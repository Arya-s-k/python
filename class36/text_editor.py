from tkinter import *
from tkinter.filedialog import askopenfile,asksaveasfile

def open_file():
    file1 = askopenfile(mode = "r",filetypes = [('text file','*.txt')])
    if file1 is not None:
        content = file1.read()
        text1.delete("1.0","end")
        text1.insert("1.0",content)
    file1.close()
    
def save_file():
    file1 = asksaveasfile(mode = "w",filetypes = [('text file','*.txt')])
    if file1 is not None:
        content = text1.get("1.0","end")
        file1.write(content)
    file1.close()

tk = Tk() 
tk.geometry("600x400") 
tk.title("text editor")
tk.configure(bg="blue")

text1 = Text(tk,width = 58,height = 20 , relief = "sunken",bg = "white")
button1 = Button(tk,text = "open",width = 10,command = open_file)
button2 = Button(tk,text = "save",width = 10,command = save_file)
button1.grid(row = 0,column= 0 ,padx = 5)
button2.grid(row = 1,column=0,pady = 5)
text1.grid(row = 0 ,column=1,rowspan=2,padx=10,pady=10)

tk.mainloop()


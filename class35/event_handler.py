from tkinter import * 

tk = Tk() 
tk.geometry("400x400") 
tk.title("event handler")
tk.configure(bg="blue")

def key_press(event): 
    print(event.char)
def mouse_click(event):
    print("Mouse clicked at")
    
    
Button1 = Button(tk, text="Click Me",bg = "blue",fg = "white")
Button1.place(x=150,y=180) 
tk.bind("<Key>", key_press)
Button1.bind("<Button-1>",mouse_click)
tk.mainloop()
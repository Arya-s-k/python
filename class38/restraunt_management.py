from tkinter import *
from datetime import datetime
#import pytz
import random

root = Tk()
root.title("Restaruant management system")
root.geometry('800x400')
root.configure(bg='beige')

frame1 = Frame(root, width = 500, height = 300, relief = SUNKEN, bg = 'beige')
frame1.pack()

label1 = Label(frame1, font=("arial",18,"bold"),text="Restaurant Management System",bg = "beige")
label1.grid(row=0,column=0,columnspan=4,padx=10,pady=10)

#timezone = pytz.timezone("Asia/Kolkata")
#datetime1 = datetime.now(timezone)
#currenttime = datetime1.strftime("%d-%m-%y %H : %M")
#labeltime = Label(frame1, text = currenttime, fg = "firebrick", font=('Times',14,'bold'),bg = "beige")
#labeltime.grid(row=1, column = 0,columnspan=4,padx=10,pady=10)

drink = StringVar()
pizza = StringVar()
burger = StringVar()
largeburger = StringVar()
fries = StringVar()

labeldrink = Label(frame1,text="Drinks",fg = "firebrick",font = ("times",12,'bold'),bg="beige")
labeldrink.grid(row=3,column=0,padx=10,pady=10)
entrydrink = Entry(frame1,textvariable=drink,justify=RIGHT)
entrydrink.grid(row=3,column=1,padx=10,pady=10)
entrydrink.insert(END,0)

labelpizza = Label(frame1,text="pizza",fg = "firebrick",font = ("times",12,'bold'),bg="beige")
labelpizza.grid(row=4,column=0,padx=10,pady=10)
entrypizza = Entry(frame1,textvariable=pizza,justify=RIGHT)
entrypizza.grid(row=4,column=1,padx=10,pady=10)
entrypizza.insert(END,0)

labelburger = Label(frame1,text="burger",fg = "firebrick",font = ("times",12,'bold'),bg="beige")
labelburger.grid(row=5,column=0,padx=10,pady=10)
entryburger = Entry(frame1,textvariable=burger,justify=RIGHT)
entryburger.grid(row=5,column=1,padx=10,pady=10)
entryburger.insert(END,0)

labellargeburger = Label(frame1,text="largeburger",fg = "firebrick",font = ("times",12,'bold'),bg="beige")
labellargeburger.grid(row=6,column=0,padx=10,pady=10)
entrylargeburger = Entry(frame1,textvariable=largeburger,justify=RIGHT)
entrylargeburger.grid(row=6,column=1,padx=10,pady=10)
entrylargeburger.insert(END,0)

labelfries = Label(frame1,text="fries",fg = "firebrick",font = ("times",12,'bold'),bg="beige")
labelfries.grid(row=7,column=0,padx=10,pady=10)
entryfries = Entry(frame1,textvariable=fries,justify=RIGHT)
entryfries.grid(row=7,column=1,padx=10,pady=10)
entryfries.insert(END,0)

#-------------------

labelorderno = Label(frame1,text="orderno",fg = "firebrick",font= ("times",12,"bold"))
labelorderno.grid(row=3,column=2)
entryorderno = Entry(frame1)
entryorderno.grid(row =3 ,column=3)

labelcost = Label(frame1,text="cost",fg = "firebrick",font= ("times",12,"bold"))
labelcost.grid(row=4,column=2)
entrycost = Entry(frame1)
entrycost.grid(row =4 ,column=3)

labelservice = Label(frame1,text="service",fg = "firebrick",font= ("times",12,"bold"))
labelservice.grid(row=5,column=2)
entryservice = Entry(frame1)
entryservice.grid(row =5 ,column=3)

labeltax = Label(frame1,text="tax",fg = "firebrick",font= ("times",12,"bold"))
labeltax.grid(row=6,column=2)
entrytax = Entry(frame1)
entrytax.grid(row =6 ,column=3)

labeltotal = Label(frame1,text="total",fg = "firebrick",font= ("times",12,"bold"))
labeltotal.grid(row=7,column=2)
entrytotal = Entry(frame1)
entrytotal.grid(row =7,column=3)











Button1 = Button(frame1,text="price",fg = "beige",font= ("times",12,"bold"),bg="firebrick",padx=10)
Button1.grid(row=10,column=0,padx=10,pady=10)
Button2 = Button(frame1,text="total",fg = "beige",font= ("times",12,"bold"),bg="firebrick",padx=10)
Button2.grid(row=10,column=1,padx=10,pady=10)
Button3 = Button(frame1,text="reset",fg = "beige",font= ("times",12,"bold"),bg="firebrick",padx=10)
Button3.grid(row=10,column=2,padx=10,pady=10)
Button4 = Button(frame1,text="exit",fg = "beige",font= ("times",12,"bold"),bg="firebrick",padx=10)
Button4.grid(row=10,column=3,padx=10,pady=10)



root.mainloop()
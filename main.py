import pace
from tkinter import *
from tkinter import ttk

def calculate(*args):
    try:
        distance_value = int(distance.get()) 
        minutes_value = int(minutes.get())
        secounds_value = int(secounds.get())
        output.set(str(secounds_value)) #確認用
    except ValueError:
        pass

root = Tk()
root.title("SpritTimeCaluculate")

frm = ttk.Frame(root, padding=10)
frm.grid()

ttk.Label(frm, text="SpritTimeCaluculater").grid(column=0, row=0)
distance = StringVar()
minutes = StringVar()
secounds = StringVar()
ttk.Entry(frm,textvariable= distance).grid(column=0,row=1)
ttk.Label(frm,text="m").grid(column=1,row=1)
ttk.Entry(frm,textvariable = minutes).grid(column=2,row=1)
ttk.Entry(frm,textvariable = secounds).grid(column=4,row=1)
ttk.Label(frm,text="min").grid(column=3,row=1)
ttk.Label(frm,text="sec").grid(column=5,row=1)

output = StringVar()
ttk.Button(frm, text="Calculate", command=calculate).grid(column=1, row=3)
ttk.Label(frm, textvariable = output).grid(column=2, row=2)
ttk.Button(frm, text="Quit", command=root.destroy).grid(column=2, row=3)
root.mainloop()

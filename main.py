import pace
from tkinter import *
from tkinter import ttk

def calculate(*args):
    try:
        value = int(distance.get()) 
        output.set(value) 
    except ValueError:
        pass

root = Tk()
root.title("SpritTimeCaluculate")
frm = ttk.Frame(root, padding=10)
frm.grid()
ttk.Label(frm, text="Hello World!").grid(column=0, row=0)
distance = StringVar()
ttk.Entry(frm,width=5, textvariable= distance).grid(column=1,row=0)
output = StringVar()
ttk.Button(frm, text="Calculate", command=calculate).grid(column=1, row=1)
ttk.Label(frm, textvariable = output).grid(column=2, row=1)
ttk.Button(frm, text="Quit", command=root.destroy).grid(column=2, row=2)
root.mainloop()

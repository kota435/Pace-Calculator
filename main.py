import pace
from tkinter import *
from tkinter import ttk

def calculate(*args):
    try:
        distance_value = int(distance.get()) 
        minutes_value = int(minutes.get())
        secounds_value = int(secounds.get())
        min_sec = minutes_value*60 + secounds_value
        distance_list = pace.create_list_distance(distance_value)
        time_list = pace.create_list_time(min_sec,distance_value)
        min_sec_list = pace.convert_to_min(time_list)

        for widget in frm2.winfo_children():
            widget.destroy()

        for i,(distance_100m,time_100m) in enumerate(zip(distance_list,min_sec_list)):
            ttk.Label(frm2,text=distance_100m).grid(column=0,row=i)
            ttk.Label(frm2,text=time_100m).grid(column=1,row=i)
    except ValueError:
        pass

root = Tk()
root.title("SplitTimeCaluculate")

frm = ttk.Frame(root, padding=10)
frm2 = ttk.Frame(root,padding=10)
frm.grid()
frm2.grid()

ttk.Label(frm, text="Split Time Caluculater").grid(column=0, row=0)
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

from tkinter import *
import var

def kreni(event):

    var.n = min(int(rows.get()), 25)
    var.m = min(int(cols.get()), 25)
    var.b = min(var.n * var.m // 2, int(boms.get()))

    var.window.quit()
    
def Custom():

    var.window = Tk()

    global rows, cols, boms
    
    rows = Entry(var.window)
    cols = Entry(var.window)
    boms = Entry(var.window)

    button = Button(var.window, text = "Kreni")
    button.bind('<Button-1>', kreni)

    rows.pack(padx = 10, pady = 10)
    cols.pack(padx = 10, pady = 10)
    boms.pack(padx = 10, pady = 10)
    button.pack(padx = 10, pady = 10)
    
    var.window.mainloop()




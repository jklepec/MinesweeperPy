from tkinter import *

import var
from Update_polja import klik

def reset(event):
    if var.Win == 1:
        return
    
    dic = event.widget.grid_info()
    x = dic['row']
    y = dic['column']
    
    temp = Label(var.new_window, image = var.polje)
    temp.bind('<Button-1>', klik)
    temp.bind('<Button-3>', zastavica)
    temp.grid(row = x, column = y)

def zastavica(event):
    if var.Win == 1:
        return
    
    dic = event.widget.grid_info()
    x = dic['row']
    y = dic['column']

    temp = Label(var.new_window, image = var.flag)
    temp.bind('<Button-3>', reset)
    temp.grid(row = x, column = y)

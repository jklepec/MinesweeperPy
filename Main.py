from tkinter import *

import var
from Igra import Init
from Podesi import Custom
from Rang import CreateLeaderboards

var.stvori()

s1 = ["Easy", "Medium", "Hard", "Custom", "Leader"]
s2 = ["Low", "High"]
P = []
L = []

def on(event):
    dic = event.widget.grid_info()
    x = dic['row']

    P[x][1].grid(row = x, column = 0, padx = 15, pady = 15)

def off(event):
    dic = event.widget.grid_info()
    if not 'row' in dic:
        return
    x = dic['row']

    P[x][1].grid_forget()

N = [9, 12, 18]
B = [10, 20, 50]

def Start(event):
    if 'new_window' in vars(var):
        var.new_window.destroy()
    
    dic = event.widget.grid_info()
    x = dic['row']

    P[x][1].grid_forget()

    if x == 3:
        Custom()
        var.window.destroy()
    else:
        var.n = N[x]
        var.m = N[x]
        var.b = B[x]

    var.mode = s1[x]
    var.ukupno = var.n * var.m - var.b

    var.new_window = Toplevel(var.prozor)
    var.new_window.resizable(False, False)
    var.new_window.title("Minesweeper")
    Init()

for i in range(5):
    P.append([])
    L.append([])
    for j in range(2):
        s = "Menu/" + s1[i] + s2[j] + ".png"
        L[i].append(PhotoImage(file = s))
        P[i].append(Label(var.prozor, image = L[i][j]))
        
    P[i][0].grid(row = i, column = 0, padx = 15, pady = 15)
    P[i][0].bind('<Enter>', on)
    P[i][1].bind('<Leave>', off)

    if i == 4:
        P[i][1].bind('<Button-1>', CreateLeaderboards)
    else:
        P[i][1].bind('<Button-1>', Start)

bomba = PhotoImage(file = "Menu/bomb.png")
Label(var.prozor, image = bomba).grid(row = 0, column = 1, rowspan = 5)

var.prozor.resizable(False, False)
var.prozor.title("Minesweeper")
var.prozor.mainloop()



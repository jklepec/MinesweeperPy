from tkinter import *
from Over import Win, Lose
import var

def ok(x, y, k):
    if x < 0 or y < 0 or x >= var.n or y >= var.m:
        return False
    if var.L[x][y] == k:
        return True
    return False

def dfs(x, y):
    if var.Win == 1:
        return
    
    if x < 0 or y < 0 or x >= var.n or y >= var.m:
        return
    
    if var.B[x][y] == 1:
        return

    var.ukupno -= 1
    
    temp = Label(var.new_window, image = var.col[var.L[x][y]])
    temp.grid(row = x + 1, column = y)
    var.B[x][y] = 1

    if var.ukupno == 0:
        Win()
        return
    
    if var.L[x][y] == 0:
        for k in range(8):
            dfs(x + var.dx[k], y + var.dy[k])

def klik(event):
    if var.Win == 1:
        return
    
    dic = event.widget.grid_info()
    x = dic['row'] - 1
    y = dic['column']

    if var.L[x][y] == -1:
        temp = Label(var.new_window, image = var.col[var.L[x][y]])
        temp.grid(row = x + 1, column = y)
        Lose()
        var.window.destroy()
        
    if var.L[x][y] >= 0:
        dfs(x, y)


from tkinter import *
from random import *

import var
from Clock import Stopwatch
from Bomba import zastavica
from Update_polja import klik

def ok(x, y, k):
    if x < 0 or y < 0 or x >= var.n or y >= var.m:
        return False
    if var.L[x][y] == k:
        return True
    return False

def Init():
    var.L = []
    var.B = []
    var.Win = 0
    var.stopwatch = 0
    
    for i in range(var.n):
        var.L.append([])
        var.B.append([])
        for j in range(var.m):
            var.L[i].append(0)
            var.B[i].append(0)
            
            temp = Label(var.new_window, image = var.polje)
            temp.bind('<Button-1>', klik)
            temp.bind('<Button-3>', zastavica)
            temp.grid(row = i + 1, column = j)
    
    for i in range(var.b):
        while True:
            x = randint(0, var.n - 1)
            y = randint(0, var.m - 1)
            
            if var.L[x][y] == -1:
                continue
            var.L[x][y] = -1
            break
        
    for i in range(var.n):
        for j in range(var.m):
            if var.L[i][j] == -1:
                continue
            for k in range(8):
                if ok(i + var.dx[k], j + var.dy[k], -1):
                    var.L[i][j] += 1

    Stopwatch()


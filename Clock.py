from tkinter import *
import var

def String(Time):
    ret = ""
    ret += str(Time // 60)
    ret += ":"
    if Time % 60 >= 10:
        ret += str(Time % 60)
    else:
        ret += "0" + str(Time % 60)
    return ret

def Stopwatch():
    
    vrijeme = Label(var.new_window, text = String(var.stopwatch), font = ("Arial", 25, "italic"))
    vrijeme.grid(row = 0, column = 0, columnspan = var.m, pady = 5)
    
    var.stopwatch += 1
    if var.Win == 1:
        return
    var.new_window.after(1000, Stopwatch)

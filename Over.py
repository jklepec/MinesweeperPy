from tkinter import *
from UpisiIme import YourName
import var

# var.prozor je glavni prozor, var.new_window je prozor u kojem se igrala igra

def Win():
    YourName()
    var.window.destroy()
    var.new_window.destroy()
    return

def Izgubi(event):
    var.window.quit()
    var.new_window.destroy()

def Lose():
    var.Win = 1
    var.window = Tk()
    var.window.resizable(False, False)

    poruka = Label(var.window, text = "Opet neuspješno!")
    poruka.pack(padx = 10, pady = 10)

    button = Button(var.window, text = "Sve jasno!")
    button.bind('<Button-1>', Izgubi)
    button.pack(padx = 10, pady = 10)
    
    var.window.mainloop()

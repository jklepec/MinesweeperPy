from tkinter import *
from Clock import String
import var

def kreni(event):

    Yourname = Name.get()
    Yourname = Yourname.replace(" ", "")
    
    if len(Yourname) > 15:
        Yourname = Yourname[0:15]

    if len(Yourname) == 0:
        return
    
    File = "Leaderboard/" + var.mode + ".txt" 
    with open(File, 'a') as f:
        f.write(Yourname + ' ' + str(Time) + "\n")

    var.window.quit()
    
def YourName():

    global Time
    Time = min(3600, var.stopwatch)
    var.Win = 1
    
    var.window = Tk()
    var.window.resizable(False, False)
    
    Label(var.window, text = "Bravo, čestitam!").pack(padx = 10, pady = 10)
    Label(var.window, text = "Your time is: " + String(Time)).pack(padx = 10, pady = 10)
    
    global Name
    Name = Entry(var.window)

    button = Button(var.window, text = "Save")
    button.bind('<Button-1>', kreni)
    
    Name.pack(padx = 10, pady = 10)
    button.pack(padx = 10, pady = 10)
    
    var.window.mainloop()

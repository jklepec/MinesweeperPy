from tkinter import *
import var
from Clock import String

def custom(a, b):
    A = a.split()
    B = b.split()

    if int(A[1]) == int(B[1]):
        return A[0] < B[0]
    else:
        return int(A[1]) < int(B[1])

def CreateLeaderboards(event):

    Board = Toplevel(var.prozor)
    Board.resizable(False, False)
    
    Label(Board, text = "Easy", font = ("Arial", 25, "bold"), fg = "green", width = 15, anchor = "w") .grid(row = 0, column = 0, pady = 10, columnspan = 3)
    Label(Board, text = "Medium", font = ("Arial", 25, "bold"), fg = "blue", width = 15, anchor = "w").grid(row = 0, column = 3, pady = 10, columnspan = 3)
    Label(Board, text = "Hard", font = ("Arial", 25, "bold"), fg = "red", width = 15, anchor = "w")   .grid(row = 0, column = 6, pady = 10, columnspan = 3)

    S = ["Easy", "Medium", "Hard"]
    
    for i in range(3):
        
        file = "Leaderboard/" + S[i] + ".txt"
        lines = []
        
        with open(file) as f:
            lines = f.readlines()

        lines = [x.strip() for x in lines]
        
        for j in range(len(lines)):
            current = lines[j].split()
            lines[j] = [int(current[1]), current[0]]

        lines.sort()
        
        for j in range(5):
            
            if j < len(lines):
                
                player = Label(Board, text = lines[j][1])
                player.grid(row = j + 1, column = i * 3 + 1, sticky = "w")
                
                time = Label(Board, text = String(lines[j][0]))
                time.grid(row = j + 1, column = i * 3 + 2, padx = (20, 100), sticky = "w")

            num = Label(Board, text = str(j + 1) + ".")
            num.grid(row = j + 1, column = i * 3, sticky = "w")
    
            

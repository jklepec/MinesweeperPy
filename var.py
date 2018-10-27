from tkinter import *

def stvori():

    global prozor
    prozor = Tk()
    # glavni prozor
    
    nula  = PhotoImage(file = "Pictures/nula.png")
    jedan = PhotoImage(file = "Pictures/1.png")
    dva   = PhotoImage(file = "Pictures/2.png")
    tri   = PhotoImage(file = "Pictures/3.png")
    cetri = PhotoImage(file = "Pictures/4.png")
    pet   = PhotoImage(file = "Pictures/5.png")
    sest  = PhotoImage(file = "Pictures/6.png")
    sedam = PhotoImage(file = "Pictures/7.png")
    osam  = PhotoImage(file = "Pictures/8.png")
    devet = PhotoImage(file = "Pictures/9.png")
    bomb  = PhotoImage(file = "Pictures/bomb.png")

    global polje
    polje = PhotoImage(file = "Pictures/polje.png")
    #slika polja
    
    global flag
    flag = PhotoImage(file = "Pictures/flag.png")
    #slika zastavice
    
    global col
    col = {-1: bomb, 0: nula, 1: jedan, 2: dva, 3: tri, 4: cetri, 5: pet, 6: sest, 7: sedam, 8: osam, 9: devet}
    # mapa: broj -> Label (Label na sebi ima sliku)
    # -1 bomba
    #  0 sivo polje
    #  1... polja sa brojkom
    
    global n, m, b, ukupno, stopwatch, Win
    global L, B
    # L je lista polja 0-indeksirana u kojoj su vrijednosti polja (-1, 0, ...)
    # B je lista boolova bio ili nisam

    global dx, dy
    
    dx = [0, 0, 1, 1, 1, -1, -1, -1]
    dy = [1, -1, -1, 0, 1, -1, 0, 1]

    global new_window, window
    # new_window je prozor za igru
    # window je prozor za poruke

import os

def clear():
    os.system("mode con cols=80")
    null_ = os.system("cls")

def print_controls():
    print("== CONTROLS ====================================================================")
    print(" UP      navigate | ENTER    open")
    print(" DOWN    navigate | P        par.dir.")
import os, curses, sys

def init() -> str:
    filename = input("File: ")
    print("CookieOS text editor")

    return filename

def run(filename: str) -> bool:
    text = input()
    if text == ";quit":
        return False

    with open(filename, "a") as autosave:
        autosave.write("text")
        autosave.write("\n")

    return True

init()
run("test.txt")
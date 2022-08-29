import os

def sleep(duration):
    os.system("sleep " + str(duration))

def clear():
    os.system("clear")

def monitor():
    clear()
    print("Hello world")
    sleep(2)
    monitor()

monitor()
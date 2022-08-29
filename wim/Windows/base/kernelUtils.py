import os

class Display:
    def clear():
        null_ = os.system("cls")
        return 0

    class buffer:
        def size():
            null_ = os.system("mode con /status > x:\\temp\\s1a23.tmp")
            tempFile = open("x:\\temp\\s1a23.tmp")

            x = tempFile.read().split("\n")[4].replace("Lines:", "").replace(" ", "") + 0               # Columns
            y = tempFile.read().split("\n")[3].replace("Lines:", "").replace(" ", "") + 0               # Rows

            class x:
                Rows, Y = y
                Columns, X = x
                Total, Z = x * y
            
            return x
        
        def change_size(x, y):
            null_ = os.system("mode con cols=" + "".join(x) + " && mode con lines=" + "".join(y))
            return 0
        
        def empty():
            Display.clear()

def pause(text):
    print(text)
    null_ = os.system("pause >nul")
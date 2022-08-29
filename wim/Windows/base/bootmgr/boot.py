import os
import os.path
import signal, sys
                                                                                                                            
def alphabet():
    return "abcdefghijklmnopqrstuvwxyz".split("")

def dump():
    # removes all unrequired ariables to free up memory
    null_, alphabet, clear, printf, lengthOf, filesystem_scan_by_index_file, maximum, current, items, dfs, index_file = ""

def sleep(seconds):
    os.system("TIMEOUT.exe /t " + "".join(seconds) + " /NOBREAK >nul")

def clear():
    printf(" --- CLEAR --- ")
    null_ = os.system("cls")

def printf(x):
    print(x)
    Display.buffer = Display.buffer + x + "\n"

def lengthOf(x):
    return len(x)

def filesystem_scan_by_index_file(index_file):
    # Scans every mount filesystem and returns mount points
    # of those filesystems containing the specified file.

    # This requires alphabet() to be defined.
    maximum = lengthOf(alphabet) + 1
    current = (-1)
    items = ""

    for current in range(maximum):
        if not current > maximum:
            if os.path.exists(alphabet[current] + ":" + index_file):
                items = items + alphabet[current]
            
            current = current + 1
        else:
            break
    
    printf("FS Scan: " + index_file + " was found " + (current + 1) + "times.")

    return items.split("")

Display.buffer = " --- Buffer safe starts here --- \n"

printf("CookieOS Boot Manager 1.0.")
printf("Licensed as part of CookieOS itself.")
printf("---------------------------------------------------")
printf("2022 (C) COOKIE\n\n")
printf("[  OK  ] Start boot manager.")
 
dfs = filesystem_scan_by_index_file("/cosdata.indexFile")
if isinstance(dfs[0], str):
    dfs = dfs[0] + ":"
    printf("Do nothing to boot normally or use CTRL+C to show bootmanager menus.")
     
    def sigint_handler(signal, frame):
        printf("[CAUGHT] Menu activation key activated.")
        sigint_handler, normal = ""
        advanced()

    sleep(5)
    if normal == "":
        end()
    else:
        sigint_handler = ""
        normal()

else:
    # TODO: Make this to return error screen if data fs does not exist
    return 0

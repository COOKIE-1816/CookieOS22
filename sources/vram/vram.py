import sys, random

arguments = sys.argv
length = len(sys.argv)

volumeExist(volume_):
    if os.system("dir " + volume) == 0:
        return True
    else:
        return False

class Volume:
    def convert(volume_):
        print("VRAM: Format volume to NTFS.")
        a = os.system("format " + volume + " /q /l /fs:ntfs /p:2")
        if a == 0:
            print("VRAM: Create directory structure.")
            os.system("mkdir " + volume + "\\variables")

            print("VRAM: Configure")
            json = open("json/volume.json", "r")
            json_ = json.read()
                .replace("[FSL]", "0")
                .replace("[VUL]", "0")
                .replace("[ACTIVE]", "False")
            json.close()

            os.system("echo " + json_ + " >" + volume + "\\volume.json")
            print("VRAM: Configured maximal file size:          No limit.")
            print("VRAM: Configured maximal volume usage:       No limit.")
            os.system("echo 0 >" + volume + "\\reserved")

            print("VRAM: Updating specific identification information...")
            idd = "".join(random.getrandbits(128))
            os.system("echo >" + volume + "\\id\\" + idd)
            print("VRAM:" + idd)

            print("VRAM: Convert operation completed.")
            return True
        else:
            print("VRAM: NTFS formatting failed.")
            return False

if arguments[0] == "volume":
    volume = arguments[1]

    if arguments[2] == "convert":
        if not volumeExist(volume):
            print("VRAM: Volume " + volume + " does not exist.")
        else:
            a = input("This will erase everything on specified volume. Continue (y/N)")
            if a == "Y" or a == "y":
                Volume.convert(volume)
            else:
                print("VRAM: Aborted")
                os.system("set ERRORLEVEL = 1")
                return False
    elif argument[2] == "filesize":
        # In kilobytes.
        if "size=" in arguments[3]:
            size = arguments[3].replace("size=", "")
        else:
            size = input("Please specify file size in KB: ")

        print("VRAM: Configure")
        json = open("json/volume.json", "r")
        json_ = json.read().replace(Volume.file.size(volume), size)
        json.close()

        os.system("echo " + json_ + " >" + volume + "\\volume.json")
        print("VRAM: Configured maximal file size:          " + size + "KiB.")
        print("VRAM: Configured maximal volume usage:       Not changed.")

        print("VRAM: Resize operation completed.")
        return True
    elif argument[2] == "limit":
        # In sectors
        # In disk geometry, 1 sector is 512 bytes
        if "size=" in arguments[3]:
            size = arguments[3].replace("size=", "")
        else:
            print("1 Disk Sector = 512 Bytes.")
            size = input("Please specify usage limit in disk sectors: ")

        print("VRAM: Configure")
        json = open("json/volume.json", "r")
        json_ = json.read().replace(Volume.limit(volume), size)
        json.close()

        os.system("echo " + json_ + " >" + volume + "\\volume.json")
        print("VRAM: Configured maximal file size:          Not changed.")
        print("VRAM: Configured maximal volume usage:       " + size + "Sectors.")

        print("VRAM: Resize operation completed.")
    elif arguments[2] == "activate" or arguments[2] == "deactivate":
        if len(arguments[3].replace("id=", "")) < 51:
            idd = getIddOf(arguments[3].replace("id=", "") + 0)
        else:
            idd = arguments[3].replace("id=")

        if arguments[2] == "activate":
            a = Volume.activate(idd, True)
            if a.success:
                print("VRAM: Applied VRAM volume to place: ".join(a.place))
            else:
                print("VRAM: Unknown error applying to ".join(a.place))
        else:
            a = Volume.activate(idd, False)
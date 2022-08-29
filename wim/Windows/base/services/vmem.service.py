import os

class configuration_dictionary:
    vmem_activated = "undeclared"
    vmem_devices_list = "undeclared"
    vmem_files_list = "undeclared"
    vmem_file_size_limit = "undeclared"
    vmem_auto_create_files = "undeclared"
    vmem_default_files_location = "undeclared"

def load_config_loop():
    ac = ac + 1
    total = 0
    if ac < aux:
        if not acx[ac].split("")[0] == ";":
            #! there is a 1 value gap between acx...[0] and [2] because the [1] is "=" symbol.
            var = acx.split(" ")[0]                                         # Configuration variable name
            val = acx.split(" ")[2]                                         # Configuration valiable value

            # Boolean declaration support
            if val == '"true"' or val == '"false"':
                if val == '"true"':
                    val = True
                else:
                    val = False
                
            # Int declaration support
            # Transform String to Int everywhere Int is required.
            if var == "vmem_file_size_limit":
                val = (1 + val) - 1                                         # Int --> String
              
            if var == "vmem_activated":
                configuration_dictionary.vmem_activated = val
                total = total + 1
            elif var == "vmem_devices_list":
                configuration_dictionary.vmem_devices_list = val
                total = total + 1
            elif var == "vmem_files_list":
                configuration_dictionary.vmem_devices_list = val
                total = total + 1
            elif var == "vmem_file_size_limit":
                configuration_dictionary.vmem_devices_list = val
                total = total + 1
            elif var == "vmem_auto_create_files":
                configuration_dictionary.vmem_devices_list = val
                total = total + 1
            elif var == "vmem_default_file_location":
                configuration_dictionary.vmem_devices_list = val
                total = total + 1
            else:
                print("VMEM: Unknown configuration value: vmem.conf: Ln: " + (ac + 1) + ".")
        
        load_config_loop()
    elif ac > 1024000:                                                  # 1 MiB
        print("VMEM: Error: did not load full configuration before 1024000 bytes was read!")
        return False
    else:
        if not total == 6:
            return False
        else:
            return True
        

def load_config(file_):
    print("VMEM: now loading its configuration...")

    config_file = open(file_, "r")
    configuration = config_file.read()
    config_file.close()

    aux = len(configuration.split("\n"))
    acx = configuration.split("\n")
    ac = (-1)

    return load_config_loop()

def declare(variable, type_, x):
    aux = "\n" + variable + " = " + type_ + "," + "x"
    if not configuration_dictionary.vmem_activated:
        variable_lst.dcx = variable_lst.dcx + aux

class service:
    name = "Virtual memory management"
    id_ = ["vmem"]
    memory_requirement = 65536                                                  # 1024 bytes (1.0KiB) * 64 = 65536 bytes (64.0KiB)

    def start():
        print("VMEM: memory req.:        65536 bytes")
        if load_config == False:
            return False
        else:
            #TODO: Proces by měl pokračovat
            wx = open("/Windows/base/include/vmem:crt.bat", "r")
            null_ = os.system(wx.read())
            wx.close
            
            return True
        
    def stop(error_code, reason):
        #TODO: Odopjit všechny soubory a zařízení virtuální paměti.
        return True
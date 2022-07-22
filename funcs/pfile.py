try:
   with open(cmd[1], "r") as file:
        print(file.read())
except:
    print("ERROR: Does that file exist?")
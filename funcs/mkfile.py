try:
    with open(cmd[1], "w") as file:
        file.write(str(input(": ")))
except:
    print("ERROR: Did you specify a file name?")
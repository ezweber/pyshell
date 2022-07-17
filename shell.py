import os
import subprocess

while True:
    command = str(input("~ ")).split()

    if(command[0] == "quit"):
        print("Goodbye!")
        quit()

    if(command[0] == "mkdir"):
        try:
            os.mkdir(command[1])
        except IndexError:
            print("ERROR: You probably forgot the dir name.")

    if(command[0] == "ls"):
        print(os.listdir("./"))

    if(command[0] == "echo"):
        try:
            print(command[1])
        except IndexError:
            print("ERROR: You need something to echo.")

    if(command[0] == "rmdir"):
        try:
            os.rmdir(command[1])
        except IndexError:
            print("ERROR: You probably forgot the dir name.")

    if(command[0] == "neofetch"):
        subprocess.run(["neofetch"])

    if(command[0] == "help"):
        x = """
        Pyshell 1.0

        mkdir - Makes a directory
        rmdir - Deletes a directory
        echo - echos any text after it
        ls - Lists files and directories in the current directory
        neofetch - Displays system info
        """
        print(x)




import os
import subprocess
import socket

def quit_sh():
    print("Goodbye!")
    quit()

def help():
    x = """
        Pyshell 1.0.1

        quit - Exits Pyshell
        mkdir - Makes a directory
        rmdir - Deletes a directory
        echo - echos any text after it
        ls - Lists files and directories in the current directory
        neoneofetch - Displays system info
        sub - Runs shell commands
        """
    print(x)

def subpro(command):
    subprocess.run(command[1])

def mkdir(command):
    try:
        os.mkdir(command[1])
    except IndexError:
        print("ERROR: You probably forgot the dir name.")

def rmdir(command):
    try:
        os.rmdir(command[1])
    except IndexError:
        print("ERROR: You probably forgot the dir name.")

def echo(command):
    try:
        print(command[1])
    except IndexError:
        print("ERROR: You need something to echo.")

def mkfile(command):
    try:
        with open(command[1], "w") as file:
            file.write(str(input(": ")))
    except:
        print("ERROR: Did you specify a file name?")

def rmfile(command):
    try:
        os.remove(command[1])
    except:
        print("ERROR: Did you type the file name correctly?")

def pfile(command):
    try:
       with open(command[1], "r") as file:
            print(file.read())
    except:
        print("ERROR: Does that file exist?") 

while True:
    command = str(input("[" + socket.gethostname() + "] ")).split()

    if(command[0] == "quit"):
        quit_sh()

    elif(command[0] == "mkdir"):
        mkdir(command)

    elif(command[0] == "ls"):
        print(os.listdir("./"))

    elif(command[0] == "echo"):
        echo(command)

    elif(command[0] == "rmdir"):
        rmdir(command)

    elif(command[0] == "neoneofetch"):
        subprocess.run(["neoneofetch"])

    elif(command[0] == "help"):
        help()

    elif(command[0] == "sub"):
        subpro(command)

    elif(command[0] == "mkfile"):
        mkfile(command)

    elif(command[0] == "rmfile"):
        rmfile(command)
    
    elif(command[0] == "pfile"):
        pfile(command)

    else:
        print("Command not found, try \"help\"")

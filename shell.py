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
        cd - Change working directory
        sub - Runs shell commands
        mkfile - Creates a file and asks for text input
        rmfile - Deletes a file
        pfile - Prints the contents of a file
        clear - Clears the screen
        """
    print(x)

def subpro(command):
    try:
        subprocess.run(command[1])
    except FileNotFoundError:
        print("That command does not exist.")

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

def cd(command):
    try:
        os.chdir(command[1])
    except FileNotFoundError:
        print("ERROR: Directory doesn't exist.")
    except NotADirectoryError:
        print("ERROR: That is not a directory")

def ls():
    print(*os.listdir("./"), sep = "\n")

def clear():
    for x in range(100):
        print("\n")
    
os.chdir(os.environ['HOME'])

while True:
    command = str(input("[" + "\033[92m" + socket.gethostname() + " " + os.getcwd() + "\033[00m" + "] ")).split()

    if(command[0] == "quit"):
        quit_sh()

    elif(command[0] == "mkdir"):
        mkdir(command)

    elif(command[0] == "ls"):
        ls()

    elif(command[0] == "echo"):
        echo(command)

    elif(command[0] == "rmdir"):
        rmdir(command)

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

    elif(command[0] == "cd"):
        cd(command)
    
    elif(command[0] == "clear"):
        clear()

    else:
        print("Command not found, try \"help\"")

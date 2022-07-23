#/usr/bin/env python

import os
import socket
import subprocess

home_path = os.path.expanduser("~")

try:
    functions = os.listdir(f"{home_path}/funcs")
except FileNotFoundError:
    print("You need the 'funcs' directory in your home directory.")
    quit()

# Sets the current working directory to the users home at startup
os.chdir(home_path)

while True:
    # Gets the command and displays the hostname and path
    cmd = str(input(f"[\033[92m{socket.gethostname()} {os.getcwd()}\033[00m] ")).split()

    # Checks if the command is the in the funcs directory and runs it.
    if cmd[0] + ".py" in functions:
        exec(open(f"funcs/{cmd[0]}.py").read())
    else:
        print(f"The command {cmd[0]} doesn't exist.")

#/usr/bin/env python

import os
import socket
import subprocess

functions = os.listdir("funcs")

# Sets the current working directory to the users home at startup
os.chdir(os.environ['HOME'])

while True:
    # Gets the command and displays the hostname and path
    cmd = str(input(f"[\033[92m{socket.gethostname()} {os.getcwd()}\033[00m] ")).split()

    if cmd[0] + ".py" in functions:
        exec(open(f"funcs/{cmd[0]}.py").read())
    else:
        print(f"The command {cmd[0]} doesn't exist.")

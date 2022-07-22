try:
    os.chdir(cmd[1])
except FileNotFoundError:
    print("ERROR: Directory doesn't exist.")
except NotADirectoryError:
    print("ERROR: That is not a directory")
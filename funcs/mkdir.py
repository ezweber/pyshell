try:
    os.mkdir(cmd[1])
except IndexError:
    print("ERROR: You probably forgot the dir name.")
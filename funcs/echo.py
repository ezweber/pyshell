try:
    print(cmd[1])
except IndexError:
    print("ERROR: You need something to echo.")
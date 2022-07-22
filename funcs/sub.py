try:
    subprocess.run(cmd[1])
except FileNotFoundError:
    print("That command does not exist.")
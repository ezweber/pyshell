del cmd[0]

#sub_cmd = ' '.join(cmd)

#print(sub_cmd)

try:
    subprocess.run(cmd)
except FileNotFoundError:
    print("That command does not exist.")
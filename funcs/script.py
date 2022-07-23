file = f"{cmd[1]}"
count = 0

with open(file, "r") as script:
    while True:
        count += 1
        
        line = script.readline().split()

        if not line:
            break

        try:
            cmd = line
            exec(open(f"funcs/{line[0]}.py").read())
        except FileNotFoundError:
            print("Invaild command in script.")
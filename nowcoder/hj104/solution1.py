while True:
    try:
        n = int(input().strip())
        for i in range(n):
            line = input().strip()
            while len(line) > 8:
                print(line[:8])
                line = line[8:]
            print(line.ljust(8, "0"))
    except:
        break

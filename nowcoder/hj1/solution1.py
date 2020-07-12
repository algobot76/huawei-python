while True:
    try:
        s = input().strip()
        print(len(s.split()[-1]))
    except:
        break

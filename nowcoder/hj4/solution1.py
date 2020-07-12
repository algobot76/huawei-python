def print_str(s):
    if len(s) <= 8:
        print(s + "0" * (8 - len(s)))
    else:
        while len(s) > 8:
            print(s[:8])
            s = s[8:]
        print(s + "0" * (8 - len(s)))


while True:
    try:
        a = input().strip()
        b = input().strip()
        print_str(a)
        print_str(b)
    except:
        break

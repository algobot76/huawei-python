while True:
    try:
        s = input().strip()
        letters = set()
        for ch in s:
            letters.add(ch)
        print(len(letters))
    except:
        break

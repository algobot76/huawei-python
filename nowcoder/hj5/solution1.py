d = {
    "A": 10,
    "B": 11,
    "C": 12,
    "D": 13,
    "E": 14,
    "F": 15
}

while True:
    try:
        num = input().strip()[2:]
        ans = 0
        for i in range(0, len(num)):
            ch = num[len(num) - 1 - i]
            n = 0
            if ch.isalpha():
                n = d[ch]
            else:
                n = int(ch)
            ans += n * (16 ** i)
        print(ans)
    except:
        break

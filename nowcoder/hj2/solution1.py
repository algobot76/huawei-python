from collections import Counter

while True:
    try:
        s = input().strip()
        ch = input().strip()
        c = Counter(s.lower())
        print(c[ch.lower()])
    except:
        break

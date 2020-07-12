from collections import Counter

s = input().strip()
ch = input().strip()
c = Counter(s.lower())
print(c[ch.lower()])

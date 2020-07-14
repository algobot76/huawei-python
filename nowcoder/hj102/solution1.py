import collections

while True:
    try:
        s = input().strip()
        c = collections.Counter(s)
        sorted_items = sorted(c.items(), key=lambda x: (-x[1], x[0]))
        print(''.join([item[0] for item in sorted_items]))
    except:
        break

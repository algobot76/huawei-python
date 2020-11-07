while True:
    try:
        n = int(input().strip())
        ans = []
        for i in range(n):
            res = []
            s = input().strip()
            for ch in s:
                if len(res) >= 2 and ch == res[-1] == res[-2]:
                    continue
                elif len(res) >= 3 and ch == res[-1] and res[-2] == res[-3]:
                    continue
                else:
                    res.append(ch)
            ans.append("".join(res))
        for s in ans:
            print(s)
    except:
        break

while True:
    try:
        num = input().strip()
        s = set()
        ans = ""
        for i in range(len(num)):
            digit = num[len(num) - 1 - i]
            if digit not in s:
                s.add(digit)
                ans += digit
        print(ans)
    except:
        break

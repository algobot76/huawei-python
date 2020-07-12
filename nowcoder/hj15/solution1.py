while True:
    try:
        num = int(input().strip())
        ans = 0
        while num:
            ans += 1
            num &= num - 1
        print(ans)
    except:
        break

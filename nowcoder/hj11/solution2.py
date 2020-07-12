while True:
    try:
        num = int(input().strip())
        ans = ""
        while num:
            ans += str(num % 10)
            num //= 10
        print(ans)
    except:
        break

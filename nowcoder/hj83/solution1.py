while True:
    try:
        r, c = input().strip().split()
        r = int(r)
        c = int(c)

        r1, c1, r2, c2 = input().strip().split()
        r1 = int(r1)
        c1 = int(c1)
        r2 = int(r2)
        c2 = int(c2)

        r3 = int(input().strip())

        c3 = int(input().strip())

        r4, c4 = input().strip().split()
        r4 = int(r4)
        c4 = int(c4)

        if r < 10 and c < 10:
            print(0)
        else:
            print(-1)

        def is_valid_r(i):
            return i in range(0, r)

        def is_valid_c(j):
            return j in range(0, c)

        def is_valid(i, j):
            return is_valid_r(i) and is_valid_c(j)

        if is_valid(r1, c1) and is_valid(r2, c2):
            print(0)
        else:
            print(-1)

        if is_valid_r(r3):
            print(0)
        else:
            print(-1)

        if is_valid_c(c3):
            print(0)
        else:
            print(-1)

        if is_valid(r4, c4):
            print(0)
        else:
            print(-1)
    except:
        break

while True:
    try:
        _ = input()
        nums = list(map(int, input().strip().split()))
        flag = int(input().strip())
        if flag == 0:
            print(' '.join(map(str, sorted(nums))))
        else:
            print(' '.join(map(str, sorted(nums, reverse=True))))
    except:
        break

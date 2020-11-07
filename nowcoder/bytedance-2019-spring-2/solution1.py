while True:
    try:
        n, d = list(map(int, input().strip().split()))
        nums = list(map(int, input().strip().split()))
        left = 0
        right = 2

        ans = 0
        while left < n - 2:
            while right < n and nums[right] - nums[left] <= d:
                right += 1
            if right - 1 - left >= 2:
                count = right - left - 1
                ans += count * (count - 1) // 2
            left += 1
        print(ans % 99997867)
    except:
        break

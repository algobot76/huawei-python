import sys

if __name__ == "__main__":
    num = int(sys.stdin.readline().strip())
    ans = 0
    while num:
        ans += 1
        num &= num - 1
    print(ans)

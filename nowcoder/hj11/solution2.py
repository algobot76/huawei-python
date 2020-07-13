import sys

if __name__ == "__main__":
    num = int(sys.stdin.readline().strip())
    ans = ""
    while num:
        ans += str(num % 10)
        num //= 10
    print(ans)

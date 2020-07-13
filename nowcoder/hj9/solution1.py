import sys

if __name__ == "__main__":
    num = sys.stdin.readline().strip()
    s = set()
    ans = ""
    for i in range(len(num)):
        digit = num[len(num) - 1 - i]
        if digit not in s:
            s.add(digit)
            ans += digit
    print(ans)

import sys

if __name__ == "__main__":
    n = int(sys.stdin.readline().strip())
    strings = []
    for _ in range(n):
        strings.append(sys.stdin.readline().strip())
    for s in sorted(strings):
        print(s)

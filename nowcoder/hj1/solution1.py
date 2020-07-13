import sys

if __name__ == "__main__":
    s = sys.stdin.readline().strip()
    print(len(s.split()[-1]))

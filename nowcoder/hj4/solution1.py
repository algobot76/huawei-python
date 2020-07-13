import sys


def print_str(s):
    if len(s) <= 8:
        print(s + "0" * (8 - len(s)))
    else:
        while len(s) > 8:
            print(s[:8])
            s = s[8:]
        print(s + "0" * (8 - len(s)))


if __name__ == "__main__":
    a = sys.stdin.readline().strip()
    b = sys.stdin.readline().strip()
    print_str(a)
    print_str(b)

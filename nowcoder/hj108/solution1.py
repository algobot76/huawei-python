import sys


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def lcm(a, b):
    return (a * b) // gcd(a, b)


if __name__ == "__main__":
    s = sys.stdin.readline().strip()
    a, b = list(map(int, s.split()))
    print(lcm(a, b))

import collections
import sys

if __name__ == "__main__":
    s = sys.stdin.readline().strip()
    ch = sys.stdin.readline().strip()
    c = collections.Counter(s.lower())
    print(c[ch.lower()])

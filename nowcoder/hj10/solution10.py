import sys

if __name__ == "__main__":
    s = sys.stdin.readline().strip()
    letters = set()
    for ch in s:
        letters.add(ch)
    print(len(letters))

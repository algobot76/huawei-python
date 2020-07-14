import sys

if __name__ == "__main__":
    line = sys.stdin.readline().strip()
    words = line.split(' ')
    print(' '.join([word[::-1] for word in reversed(words)]))

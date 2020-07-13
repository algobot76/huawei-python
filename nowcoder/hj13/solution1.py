import sys

if __name__ == "__main__":
    sentence = sys.stdin.readline().strip()
    print(' '.join(sentence.split()[::-1]))

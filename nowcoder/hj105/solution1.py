import sys

if __name__ == "__main__":
    neg = []
    pos = []
    nums = list(map(int, sys.stdin.readline().strip().split()))
    for n in nums:
        if n < 0:
            neg.append(n)
        else:
            pos.append(n)
    print(len(neg))
    if pos:
        print("{:.1f}".format(sum(pos) / len(pos)))
    else:
        print("0.0")

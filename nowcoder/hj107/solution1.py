import sys

if __name__ == "__main__":
    num = float(sys.stdin.readline().strip())
    e = 0.0001
    temp = num
    while abs(temp ** 3 - num) > e:
        temp = temp - (temp ** 3 - num) * 0.1 / (3 * temp ** 2)
    print("%.1f" % temp)

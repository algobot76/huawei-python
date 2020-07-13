import sys

if __name__ == "__main__":
    logs = []
    for line in sys.stdin:
        line = line.strip().split()
        filename = line[0].split("\\")[-1]
        if len(filename) > 16:
            filename = filename[-16:]
        line_no = line[1]
        search = [l for l in logs if l[0] == filename and l[1] == line_no]
        if search:
            idx = logs.index(search[0])
            (_, _, count) = search[0]
            logs[idx] = (filename, line_no, count + 1)
        else:
            logs.append((filename, line_no, 1))
    for l in logs[-8:]:
        print("{} {} {}".format(l[0], l[1], l[2]))

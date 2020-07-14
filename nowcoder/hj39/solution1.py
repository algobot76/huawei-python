import re
import sys


def is_legal_ip(ip):
    if not ip:
        return False

    pattern = re.compile(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$")
    if not pattern.match(ip):
        return False

    segments = ip.split(".")
    for s in segments:
        s = int(s)
        if s < 0 or s > 255:
            return False

    return True


def is_private_ip(ip):
    if not is_legal_ip(ip):
        return False

    segments = ip.split(".")
    s0 = int(segments[0])
    s1 = int(segments[1])
    if s0 == 10:
        return True
    if s0 == 172:
        if 16 <= s1 <= 31:
            return True
    if s0 == 192 and s1 == 168:
        return True

    return False


def is_legal_mask(mask):
    if not is_legal_ip(mask):
        return False

    bin_mask = "".join(
        [format(int(segment), 'b') for segment in mask.split(".")])
    first_zero_idx = bin_mask.find("0")
    last_one_idx = bin_mask.rfind("1")
    if first_zero_idx == -1 or last_one_idx == -1:
        return False
    if last_one_idx > first_zero_idx:
        return False
    return True


def ip_category(ip):
    if not is_legal_ip(ip):
        raise ValueError("Illegal IP")

    s0 = int(ip.split(".")[0])
    if 1 <= s0 <= 126:
        return "A"
    if 128 <= s0 <= 191:
        return "B"
    if 192 <= s0 <= 223:
        return "C"
    if 224 <= s0 <= 239:
        return "D"
    if 240 <= s0 <= 255:
        return "E"

    raise ValueError("Unknown category")


if __name__ == "__main__":
    a = 0
    b = 0
    c = 0
    d = 0
    e = 0
    f = 0
    p = 0
    for line in sys.stdin:
        ip, mask = line.strip().split("~")
        if not is_legal_ip(ip) or not is_legal_mask(mask):
            f += 1
        else:
            if is_private_ip(ip):
                p += 1
            try:
                category = ip_category(ip)
                if category == "A":
                    a += 1
                if category == "B":
                    b += 1
                if category == "C":
                    c += 1
                if category == "D":
                    d += 1
                if category == "E":
                    e += 1
            except ValueError:
                pass
    print(a, b, c, d, e, f, p)

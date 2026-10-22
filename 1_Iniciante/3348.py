import math
import sys

def resolver():

    entrada = sys.stdin.read().split()
    if not entrada:
        return

    n = int(entrada[0])

    k = 1
    for i in range(n + 1, 2 * n + 1):
        k = math.lcm(k, i)

    print(k)

if __name__ == "__main__":
    resolver()
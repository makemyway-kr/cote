import sys
from itertools import combinations


def solution():
    temp = sys.stdin.readline().rstrip().split(' ')
    n = int(temp[0])
    k = int(temp[1])
    coins = []
    for i in range(n):
        temp = int(sys.stdin.readline().rstrip())
        coins.append(temp)
    values = [10001 for x in range(k+1)]
    if k < min(coins):
        print(-1)
        return 0
    elif k in coins:
        print(1)
        return 0
    for c in coins:
        for v in range(c, k+1):
            if v == c:
                values[v] = 1
                continue
            values[v] = min(values[v], values[v-c]+1)
    if values[k] == 10001:
        print(-1)
    else:
        print(values[k])


solution()

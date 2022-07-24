import sys
from itertools import product

N, M = map(int, sys.stdin.readline().rstrip().split())

per = list(product([x for x in range(1, N+1)], repeat=M))

for p in per:
    for n in p:
        print(n, end=' ')
    print()

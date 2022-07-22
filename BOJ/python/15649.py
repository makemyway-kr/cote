import sys
from itertools import permutations

N, M = map(int, sys.stdin.readline().rstrip().split())
numbers = [i for i in range(1, N+1)]

s = permutations(numbers, M)
for sp in s:
    for n in sp:
        print(n, end=' ')
    print()

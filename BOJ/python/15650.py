import sys
from itertools import combinations
N, M = map(int, sys.stdin.readline().rstrip().split())
temp = [i for i in range(1, N+1)]
answers = combinations(temp, M)
for a in answers:
    for t in a:
        print(t, end=' ')
    print()

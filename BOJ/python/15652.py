import sys
from itertools import combinations_with_replacement
N,M = map(int,sys.stdin.readline().rstrip().split())

comb = combinations_with_replacement([x for x in range(1,N+1)],M)

for c in comb:
    for i in c:
        print(i,end= ' ')
    print()
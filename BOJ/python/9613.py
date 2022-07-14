from itertools import combinations
from math import gcd
import sys
T = int(sys.stdin.readline().rstrip())
for t in range(T):
    temp = [int(x) for x in sys.stdin.readline().rstrip().split()]
    C = combinations(temp[1:],2)
    answer = 0
    for c in C:
        answer += gcd(c[0],c[1])
    print(answer)
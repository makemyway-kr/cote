import sys
from itertools import permutations


def solution():
    N = int(sys.stdin.readline().rstrip())
    wage = []
    answer = 1000001 * N
    for i in range(N):
        temp = [int(x) for x in sys.stdin.readline().rstrip().split(' ')]
        wage.append(temp)
    nodes = [x for x in range(N)]
    nodes = permutations(nodes, N)
    for n in nodes:
        temp = 0
        if wage[n[-1]][n[0]] == 0:
            continue
        for c in range(N):
            if c == N-1:
                temp += wage[n[c]][n[0]]
                if temp < answer:
                    answer = temp
            elif wage[n[c]][n[c+1]] != 0:
                temp += wage[n[c]][n[c+1]]
            else:
                break
    print(answer)


solution()

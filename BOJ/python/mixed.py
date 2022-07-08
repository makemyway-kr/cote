# 25312번
import sys
import heapq


def solution():
    N, M = map(int, sys.stdin.readline().rstrip.split(' '))
    juices = []
    for i in range(N):
        temp = [int(x) for x in sys.stdin.readline().rstrip.split(' ')]
        heapq.heappush(juices, (-(temp[1]/temp[0]), temp))
    Q = 0
    answer = []
    while Q != M:
        j = heapq.heappop(juices)
        if j[1][1] == M:
            answer = [j[1][0], 1]
            break
        if Q + j[1][1] >= M:

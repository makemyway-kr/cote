import sys
import heapq


def solution():
    temp = sys.stdin.readline().rstrip().split(' ')
    N = int(temp[0])
    M = int(temp[1])
    temp = [int(x) for x in sys.stdin.readline().rstrip().split(' ')]
    hq = []
    for t in temp:
        heapq.heappush(hq, (t, t))
    for n in range(M):
        c1 = heapq.heappop(hq)
        c2 = heapq.heappop(hq)
        heapq.heappush(hq, (c1[0]+c2[0], c1[1]))
        heapq.heappush(hq, (c1[0]+c2[0], c2[1]))
    answer = 0
    for n in range(N):
        answer += heapq.heappop(hq)[0]
    print(answer)


solution()

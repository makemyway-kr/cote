import sys
import heapq


def solution():
    N = int(sys.stdin.readline().rstrip())
    heap = []
    for i in range(N):
        temp = int(sys.stdin.readline().rstrip())
        if temp == 0:
            if len(heap) == 0:
                print(0)
            else:
                print(heapq.heappop(heap)[1])
        else:
            heapq.heappush(heap, (abs(temp), temp))


solution()

import heapq
import sys


def solution():
    heapArr = []
    N = int(sys.stdin.readline().rstrip())
    for i in range(N):
        temp = int(sys.stdin.readline().rstrip())
        if temp == 0:
            if len(heapArr) == 0:
                print(0)
            else:
                print(heapq.heappop(heapArr))
        else:
            heapq.heappush(heapArr, temp)


solution()

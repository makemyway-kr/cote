from re import L
import sys


def solution():
    N, M = map(int, sys.stdin.readline().rstrip().split(' '))
    numbers = []
    for i in range(N):
        numbers.append(int(sys.stdin.readline().rstrip()))
    numbers.sort()
    minimum = 100000000001
    i, k = 0, 1
    while i < N-1 and k < N:
        if numbers[k]-numbers[i] < M:
            k += 1
        elif numbers[k] - numbers[i] == M:
            minimum = M
            break
        else:
            minimum = min(minimum, numbers[k] - numbers[i])
            i += 1
    print(minimum)


solution()

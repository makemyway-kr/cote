import sys

N, K = map(int, sys.stdin.readline().rstrip().split())
things = []
answer = 0
prices = [0 for x in range(1, K+1)]

for n in range(N):
    w, p = map(int, sys.stdin.readline().rstrip().split())
    things.append((w, p))
things.sort(key=lambda x: x[0])

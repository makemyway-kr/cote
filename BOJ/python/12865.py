import sys

N,K = map(int,sys.stdin.readline().rstrip().split())
things = []
bags = {x:[] for x in range(1,N+1)}

for n in range(N):
    w,p = map(int,sys.stdin.readline().rstrip().split())
    things.append((w,p))


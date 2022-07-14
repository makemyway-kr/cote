import sys
T = int(sys.stdin.readline().rstrip())

for t in range(T):
    N,M = map(int,sys.stdin.readline().rstrip().split(' '))
    for m in range(M):
        a,b = map(int,sys.stdin.readline().rstrip().split(' '))
    print(N-1)
    #연결그래프이므로 항상 N-1
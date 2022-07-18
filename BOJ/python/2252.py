import sys
N,M = map(int,sys.stdin.readline().rstrip().split())
graphs = [0 for i in range(N)]

for i in range(M):
    a,b = map(int,sys.stdin.readline().rstrip().split())
    graphs[b-1] += 1
students = [i for i in range(1,N+1)]
students.sort(key = lambda x : graphs[x-1])
for s in range(0,N):
    if s != N-1:
        print(students[s],end=' ')
    else:
        print(students[s])
import sys
N,K = map(int,sys.stdin.readline().rstrip().split())
students = [int(x) for x in sys.stdin.readline().rstrip().split()]

diffs = []

for s in range(N-1):
    diffs.append(students[s+1]-students[s])
diffs.sort()
print(sum(diffs[:N-K]))
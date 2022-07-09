import sys

N = int(sys.stdin.readline().rstrip())
s = 0
sums = []
temp = [int(x) for x in sys.stdin.readline().rstrip().split(' ')]
for i in range(N):
    s += temp[i]
    sums.append(s)
M = int(sys.stdin.readline().rstrip())
for i in range(M):
    left, right = map(int, sys.stdin.readline().rstrip().split(' '))
    if left == 1:
        print(sums[right-1])
    else:
        print(sums[right-1]-sums[left-2])

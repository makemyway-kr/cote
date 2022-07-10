# 1946번
import sys

T = int(sys.stdin.readline().rstrip())
for t in range(T):
    people = []
    N = int(sys.stdin.readline().rstrip())
    for n in range(N):
        temp = [int(x) for x in sys.stdin.readline().rstrip().split(' ')]
        people.append(temp)

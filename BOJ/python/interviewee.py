# 1946번
import sys

T = int(sys.stdin.readline().rstrip())
for t in range(T):
    people = []
    drop = []
    N = int(sys.stdin.readline().rstrip())
    for n in range(N):
        temp = [int(x) for x in sys.stdin.readline().rstrip().split(' ')]
        people.append(temp)
    people.sort(key=lambda x: x[0])
    for p in range(N-1):
        if p in drop:
            continue
        for p2 in range(p+1, N):
            if (p2 not in drop) and (people[p][0] > people[p2][0]) and (people[p][1] > people[p2][1]):
                drop.append(p2)
    print(N-len(drop))

import sys
T = int(sys.stdin.readline().rstrip())
for t in range(T):
    scores = []
    answer = 1
    N = int(sys.stdin.readline().rstrip())
    for n in range(N):
        t1,t2 = map(int,sys.stdin.readline().rstrip().split(' '))
        scores.append([t1,t2])
    scores.sort(key = lambda x : x[0])
    top = 0
    for s in range(1,len(scores)):
        if scores[top][1] > scores[s][1]:
            answer += 1
            top = s
    print(answer)

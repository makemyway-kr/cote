import sys


def solution():
    N = int(sys.stdin.readline().rstrip())
    meetings = []
    for i in range(N):
        meetings.append([int(x)
                        for x in sys.stdin.readline().rstrip().split(' ')])
    answer = 0
    curr = 0
    meetings.sort(key=lambda x: x[0])
    meetings.sort(key=lambda x: x[1])
    for m in meetings:
        if m[1] >= curr and m[0] >= curr:
            curr = m[1]
            answer += 1
    print(answer)


solution()

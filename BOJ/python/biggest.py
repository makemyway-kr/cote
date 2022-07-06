import sys


def solution():
    temp = sys.stdin.readline().rstrip().split(' ')
    N = int(temp[0])
    M = int(temp[1])
    numbers = []
    answers = []
    ranges = []
    for i in range(1, N+1):
        numbers.append(int(sys.stdin.readline().rstrip()))
    for i in range(M):
        ranges.append(sys.stdin.readline().rstrip().split(' '))
    for r in ranges:
        a = int(r[0])
        b = int(r[1])
        tanswer = []
        temp = numbers[a-1:b]
        tanswer.append(min(temp))
        tanswer.append(max(temp))
        answers.append(tanswer)
    for a in answers:
        print(str(a[0])+' '+str(a[1]))


solution()

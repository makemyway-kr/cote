import sys
N = int(sys.stdin.readline().rstrip())
for i in range(N):
    temp = [int(x) for x in sys.stdin.readline().rstrip().split()]
    average = sum(temp[1:])/temp[0]
    over_averages = 0
    for p in temp[1:]:
        if p > average:
            over_averages += 1
    answer = str(round((over_averages/temp[0])*100, 3))
    if len(answer.split('.')[1]) == 1:
        answer += '00%'
    elif len(answer.split('.')[1]) == 2:
        answer += '0%'
    else:
        answer += '%'
    print(answer)

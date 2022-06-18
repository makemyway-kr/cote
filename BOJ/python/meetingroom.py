def solution():
    m = int(input())
    meetings = []
    for i in range(m):
        temp = input()
        temp = temp.split(' ')
        meetings.append([int(temp[0]),int(temp[1])])
    meetings.sort(key = lambda x : x[1]-x[0])
    meetings.sort(key = lambda x : x[0])
    answer = 0
    curr = meetings[0][0]
    print(meetings)
    for i in meetings:
        if curr >= i[0]:
            answer += 1
            curr = i[1]
    print(answer)
solution()
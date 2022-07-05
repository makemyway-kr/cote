def solution():
    temp = input().split(' ')
    N = int(temp[0])
    M = int(temp[1])
    numbers= []
    answers = []
    ranges = []
    for i in range(1,N+1):
        numbers.append([int(input()),i])
    for i in range(M):
        rinput = input().split(' ')
        ranges.append(rinput)
    numbers.sort(key = lambda x : x[0])
    for r in ranges:
        a = int(r[0])
        b = int(r[1])
        tanswer = []
        print(a,b)
        for n in range(len(numbers)):
            if numbers[n][1] >= a and numbers[n][1] <= b:
                tanswer.append(numbers[n][0])
                break
        for n in range(len(numbers)-1,-1,-1):
            if numbers[n][1] >= a and numbers[n][1] <= b:
                tanswer.append(numbers[n][0])
                break
        answers.append(tanswer)
    for a in answers:
        print(str(a[0])+' '+str(a[1]))
solution()
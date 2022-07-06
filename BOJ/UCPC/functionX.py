def solution():
    Q = int(input())
    functions = []
    for i in range(Q):
        temp = input().split(' ')
        if temp[0] == '1':
            functions.append([int(temp[1]), int(temp[2])])
        else:
            temp = int(temp[1])
            answer = 1
            for f in functions:
                y = (f[0]*temp) + f[1]
                if y == 0:
                    answer = 0
                    break
                elif (y < 0 and answer == -1) or (y > 0 and answer == 1):
                    answer = 1
                else:
                    answer = -1
            if answer == -1:
                print('-')
            elif answer == 0:
                print(0)
            else:
                print('+')


solution()

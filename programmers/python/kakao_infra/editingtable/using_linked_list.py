def solution(n, k, cmd):
    answer = ['O' for x in range(n)]
    temp = [[x-1,x+1] for x in range (n)]
    start = 0
    last = n-1
    curr = k
    last_deleted = []
    for c in cmd:
        if c[0] == 'C':
            answer[curr] = "X"
            last_deleted.append(curr)
            if temp[curr][0] == -1: #제일 앞
                temp[temp[curr][1]][0] = -1
                curr = temp[curr][1]
                start = curr
            elif temp[curr][1] == n : #제일 끝
                curr = temp[curr][0]
                temp[curr][1] = n
                last = curr
            else:
                temp[temp[curr][0]][1]=temp[curr][1]
                temp[temp[curr][1]][0] = temp[curr][0]
                curr = temp[curr][1]
        elif c[0] == 'Z':
            to_recover = last_deleted.pop()
            if to_recover<start: #맨앞 복구
                temp[to_recover][0] = -1
                temp[to_recover][1] = start
                temp[start][0] = to_recover
                start = to_recover
            elif to_recover > last: #맨 뒤 복구
                temp[to_recover][1] = n
                temp[to_recover][0] = last
                temp[last][1] = to_recover
                last = to_recover
            else:
                if to_recover < int(n/2): #중간을 기준으로 앞에 있으면 앞쪽에서 지워지지 않은 행이 발견될 확률이 높음.
                    for i in range(to_recover-1,start-1,-1):
                        if answer[i] == "O":
                            temp[to_recover][0] = i
                            temp[to_recover][1] = temp[i][1]
                            temp[temp[i][1]][0] = to_recover
                            temp[i][1] = to_recover
                            break
                else:
                    for i in range(to_recover+1,last+1):
                        if answer[i] == "O":
                            temp[to_recover][1] = i
                            temp[to_recover][0] = temp[i][0]
                            temp[temp[i][0]][1] = to_recover
                            temp[i][0] = to_recover
                            break
            answer[to_recover] = "O"
        else:
            to_move = int(c.split(' ')[1])
            if c[0] == 'D':
                for i in range(to_move):
                    curr = temp[curr][1]
            elif c[0] == 'U':
                for i in range(to_move):
                    curr = temp[curr][0]
    return "".join(answer)
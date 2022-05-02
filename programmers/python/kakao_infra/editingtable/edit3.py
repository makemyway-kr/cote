from operator import indexOf

def solution(n, k, cmd):
    answer = ''
    temp = [1 for f in range (n)]
    live = [x for x in range(n)]
    curr = k
    last_deleted = []
    for c in cmd:
        if c[0] == 'C':
            temp[curr] = 0
            last_deleted.append(curr)
            if curr == live[-1]:
                curr = live[-2]
            else:
                curr = live[indexOf(live,last_deleted[-1])+1]
            live.pop(indexOf(live,last_deleted[-1]))
        elif c[0] == 'Z':
            to_recover = last_deleted.pop()
            live.append(to_recover)
            live.sort()
            temp[to_recover] = 1
        else:
            to_move = int(c.split(' ')[1])
            if c[0] == 'D':
                curr = live[indexOf(live,curr)+to_move]
            elif c[0] == 'U':
                curr = live[indexOf(live,curr)-to_move]
    for i in temp:
        if i == 1:
            answer+="O"
        else:
            answer+="X"
    return answer

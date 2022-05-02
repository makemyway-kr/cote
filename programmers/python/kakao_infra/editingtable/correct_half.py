def solution(n, k, cmd):
    answer = ''
    temp = [1 for f in range (n)]
    start = 0
    last = n-1
    curr = k
    last_deleted = []
    for c in cmd:
        if c[0] == 'C':
            temp[curr] = 0
            last_deleted.append(curr)
            if curr == last : 
                for i in range(last , start-1,-1):
                    if temp[i] == 1:
                        curr = i
                        break
                last = curr
            elif curr == start:
                for i in range(start , last+1):
                    if temp[i] == 1:
                        curr = i
                        break
                start = curr
            else:
                for i in range(curr,last+1):
                    if temp[i] == 1:
                        curr = i
                        break
        elif c[0] == 'Z':
            to_recover = last_deleted.pop()
            if to_recover < start :
                start = to_recover
            elif to_recover > last:
                last = to_recover
            temp[to_recover] = 1
        else:
            to_move = int(c.split(' ')[1])
            count = 0
            after = 0
            if c[0] == 'D':
                for i in range(curr+1 , last+1):
                    if temp[i] == 1:
                        count +=1
                    if count == to_move:
                        after = i
                        break
            elif c[0] == 'U':
                for i in range(curr-1 , start-1 , -1):
                    if temp[i] == 1:
                        count +=1
                    if count == to_move:
                        after = i
                        break
            curr = after
    for i in temp:
        if i == 1:
            answer+="O"
        else:
            answer+="X"
    return answer
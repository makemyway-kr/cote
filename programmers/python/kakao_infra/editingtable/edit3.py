def solution(n, k, cmd):
    answer = ''
    temp = [1 for f in range (n)]
    start = 0
    last = n-1
    curr = k
    links = [[x-1,x+1] for x in range(n)]
    last_deleted = []
    for c in cmd:
        if c[0] == 'C':
            temp[curr] = 0
            last_deleted.append(curr)
            if curr == last : 
                curr = links[curr][0]
                last = curr
                links[curr][1]=n

            elif curr == start:
                curr = links[curr][1]
                start = curr
                links[curr][0] = -1
            else:
                curr = links[curr][1]
                links[curr][0] = links[links[curr][0]][0]
                
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
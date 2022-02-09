def solution(n, edge):#BFS
    answer=0
    temp=[[]for col in range(n+1)]
    for p in edge:
        temp[p[0]].append(p[1])
        temp[p[1]].append(p[0])
    curr=1
    queue=[1]
    visitied=[]
    while len(queue)!=0:
        curr=queue.pop(0)
        count=0
        visitied.append(curr)
        for l in temp[curr]:
            if l not in queue and l not in visitied:
                queue.append(l)
                count+=1
        if count==0:#queue에 더이상 추가할 점이 없으면, 가장 먼것임
            answer+=1
    return answer
print(solution(6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]))
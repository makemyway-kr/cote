def solution(n, edge):#BFS
    answer=0
    temp=[[]for col in range(n+1)]
    for p in edge:
        temp[p[0]].append(p)
        temp[p[1]].append(p)
    curr=1
    depth=0
    queue=[1]
    depths=[0 for point in range(n+1)]
    maxdepth=0
    visitied=[]
    while len(queue)!=0:
        curr=queue.pop()
        depth=depths[curr]
        for l in temp[curr]:
            if l[0]==curr and (l[1] not in queue and l[1] not in visitied):
                queue.append(l[1])
                depths[l[1]]=depth+1
                if depths[l[1]]>maxdepth:
                    maxdepth=depths[l[1]]
            elif l[1]==curr and (l[0] not in queue and l[0] not in visitied):
                queue.append(l[0])
                depths[l[0]]=depth+1
                if depth+1>maxdepth:
                    maxdepth=depth+1
        visitied.append(curr)
    for p in depths:
        if p==maxdepth:
            answer+=1
    return answer
solution(6,[[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]])
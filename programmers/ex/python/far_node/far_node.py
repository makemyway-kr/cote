def solution(n, edge):
    answer = 0
    visited=[]
    curr=1
    depth=0
    visit=1
    start_from=0
    while visit!=n:
        temp=[]
        for k in edge:
            if curr in k:
                to_insert=[]
                if k[0]==curr:
                    to_insert=[k[1],depth+1]
                elif k[1]==curr:
                    to_insert=[k[0],depth+1]
                err=0
                for j in visited:
                    if j[0]==to_insert[0]:
                        err=1
                if err==0:
                    visited.append(to_insert)
                    visit+=1
                temp.append(k)
        for k in temp:
            edge.remove(k)
        if visited[start_from][0]==curr:
            curr=visited[start_from][1]
        else:
            curr=visited[start_from][0]
        depth=visited[start_from][1]
        start_from+=1
    for l in visited:
        if depth==l[1]:
            answer+=1
    return answer
solution(6,[[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]])
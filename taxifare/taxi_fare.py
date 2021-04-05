graph=[[]]
def minnode(v):
    ans=0
    min=100001
    for i in range(1,len(v)+1):
        if v[i]<min:
            min=v[i]
            ans=i
    return ans


def dijk(start,fin,n):
    flist=[]
    visit=[]
    flist.appned(0)
    visit.appned(False)
    for i in range(1,n+1):
        if i==start:
            flist.append(0)
            visit.append(True)
        elif graph[start][i]!=100001:
            flist.append(graph[start][i])
            visit[i].append(False)
        else:
            flist.append(100001)
            visit[i].append(False)
    while visit[fin]!=True:
        curr=minnode(flist)
        visit[curr]=True
        for i in range(1,n+1):
            if flist[curr]+graph[curr][i]<flist[i]:
                flist[i]=flist[curr]+graph[curr][i]
    return flist[fin]
    


def solution(n, s, a, b, fares):
    answer = 0
    for i in range(n+1):
        for k in range(n+1):
            if i==k:
                global graph[i][k]=0
            elif i==0 or k==0:
                global graph[i][k]=0
            else:
                global graph[i][k]=100001
    for i in fares:
        global graph[i[0]][i[1]]=i[2]
        global graph[i[1]][i[0]]=i[2]
    
    return answer
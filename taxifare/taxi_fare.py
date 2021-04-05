graph=[[]]
def pre(n,fares):
    global graph
    graph=[[100001 for col in range(n+1)]for i in range(n+1)]
    for i in range(n+1):
        for k in range(n+1):
            if i==k:
                graph[i][k]=0
            elif i==0 or k==0:
                graph[i][k]=0
    for i in fares:
        graph[i[0]][i[1]]=i[2]
        graph[i[1]][i[0]]=i[2]

def minnode(v,f):
    ans=0
    min=100001
    for i in range(1,len(v)):
        if f[i]<min and v[i]==False:
            min=f[i]
            ans=i
    return ans


def dijk(start,fin,n):
    flist=[0 for i in range(n+1)]
    visit=[False for i in range(n+1)]
    for i in range(1,(n+1)):
        if i==start:
            flist[i]=(100001)
            visit[i]=(True)
        elif graph[start][i]!=100001:
            flist[i]=(graph[start][i])
        else:
            flist.append(100001)
    while visit[fin]!=True:
        curr=minnode(visit,flist)
        visit[curr]=True
        for i in range(1,n+1):
            if flist[curr]+graph[curr][i]<flist[i]:
                flist[i]=flist[curr]+graph[curr][i]
    return flist[fin]
    


def solution(n, s, a, b, fares):
    answer = 10001
    pre(n,fares)
    for i in range(1,n+1):
        answer=min(answer,dijk(s,i,n)+dijk(i,a,n)+dijk(i,b,n))
    return answer
print(solution(6,4,6,2,[[4,1,10],[3,5,24],[5,6,2],[3,1,41],[5,1,24],[4,6,50],[2,4,66],[2,3,22],[1,6,25]]))
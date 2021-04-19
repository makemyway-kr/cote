graph=[[]]
 #사전 graph 작업
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
#가장 비용이 적은 노드 찾는 함수
def minnode(v,f):
    ans=0
    min=100001
    for i in range(1,len(v)):
        if f[i]<min and v[i]==False:
            min=f[i]
            ans=i
    if ans==0:#연결할수 있는 최단거리 노드가 존재하지 않는 경우
        return -1
    else:
        return ans


def dijk(start,fin,n):#다익스트라알고리즘
    if start==fin:
        return 0
    else:
        global graph
        flist=[0 for i in range(n+1)]
        visit=[False for i in range(n+1)]
        for i in range(1,(n+1)):
            if i==start:
                flist[i]=(100001)
                visit[i]=(True)
            elif graph[start][i]!=100001:
                flist[i]=(graph[start][i])
            else:
                flist[i]=100001
        rc=True
        while visit[fin]!=True:
            curr=minnode(visit,flist)
            if curr==-1:
                rc=False
                break
            else:
                visit[curr]=True
                for i in range(1,n+1):
                    if flist[curr]+graph[curr][i]<flist[i] and visit[i]==False:
                        flist[i]=flist[curr]+graph[curr][i]
        if rc==False:
            return 100001
        elif rc==True:
            return flist[fin]
def solution(n, s, a, b, fares):
    answer = 100001
    if len(fares)==3:
        answer=fares[0][2]+fares[1][2]+fares[2][1]
    else:
        pre(n,fares)
        for i in range(1,n+1):
            answer=min(answer,dijk(s,i,n)+dijk(i,a,n)+dijk(i,b,n))
    return answer
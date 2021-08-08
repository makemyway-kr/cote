import copy
def DFS(n,computers,curr,queue):
    for k in range(n):
        if computers[curr][k]==1 and k!=curr:
            if k not in queue:
                queue.append(k)
                DFS(n,computers,k,queue)

            
def solution(n, computers):
    queueofconnected=[]
    answer = 0
    for i in range (n):
        if i not in queueofconnected:
            DFS(n,computers,i,queueofconnected)
            answer+=1
    return answer

print(solution(3,[[1,1,0],[1,1,0],[0,0,1]]))
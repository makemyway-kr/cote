def can_i(a):
    sum=0
    for i in range(len(a)):
        sum+=a[i]
    if sum==0:
        return True
    else:
        return False
def startnode(a,edges):
    index=0
    for g in range(len(a)):
        if a[g]<0 and min(a[g],a[index])==a[g]:
            index=g
    for g in edges:
        if g[0]==index:
            index=g[1]
        elif g[1]==index:
            index=g[0]
    return index
    
def solution(a, edges):
    answer = -1
    count=0
    for l in range(len(a)):
        if a[l]==0:
            count+=1
    if(count==len(a)):
        answer=0
    else:
        snode=startnode(a,edges)
        for l in edges:
            
    return answer
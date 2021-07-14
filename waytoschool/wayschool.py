import time
def solution(m, n, puddles):
    start=time.time()
    answer = 0
    routes=[[0 for col in range(m+1)]for row in range(n+1)]
    curr=[1,1]
    while curr!=[m,n]:
        row=curr[0]
        col=curr[1]
        if curr not in puddles:
            routes[row][col]=routes[row-1][col]+routes[row][col-1]
        
    end=time.time()
    print(end-start)
    return answer
print(solution(4,3,[[2,2]]))
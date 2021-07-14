def solution(m, n, puddles):
    answer = 0
    routes=[[[0,0] for col in range(m+1)]for row in range(n+1)]#number of shortest routes at first and cost at second.
    for k in range(0,m+1):
        routes[0][k][1]=10001
    for k in range(0,n+1):
        routes[k][0][1]=10001
    routes[1][1]=[1,0]
    curr=[1,2]
    while curr[0]<=n:
        row=curr[0]
        col=curr[1]
        if curr not in puddles:
            value=min(routes[row-1][col][1],routes[row][col-1][1])
            routes[row][col][1]=value+1
            if value==routes[row-1][col][1] and value!=routes[row][col-1][1]:
                routes[row][col][0]=routes[row-1][col][0]
            elif value!=routes[row-1][col][1] and value==routes[row][col-1][1]:
                routes[row][col][0]=routes[row][col-1][0]
            elif value==routes[row-1][col][1] and value==routes[row][col-1][1]:
                routes[row][col][0]=routes[row-1][col][0]+routes[row][col-1][0]
        elif curr in puddles:
            routes[curr[0]][curr[1]][1]=10001
        if col==m:
            row=row+1
            col=1
        else:
            col=col+1
        curr=[row,col]
    answer=routes[n][m][0]
    return answer
print(solution(4,3,[[2,2]]))
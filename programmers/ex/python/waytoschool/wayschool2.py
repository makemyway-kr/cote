def solution(m,n,puddles):
    ways=[[0 for row in range(m)] for col in range(n)]
    ways[0][0]=1
    for row in range(0,n):
        for col in range(0,m):
            if [col+1,row+1] not in puddles and [row,col]!=[0,0]:
                if row==0:
                    ways[row][col]=ways[row][col-1]
                elif col==0:
                    ways[row][col]=ways[row-1][col]
                else:
                    ways[row][col]=ways[row-1][col]+ways[row][col-1]
    answer=ways[n-1][m-1]%1000000007
    return answer
print(solution(4,3,[[2,2]]))
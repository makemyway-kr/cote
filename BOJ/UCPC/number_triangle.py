def solution():
    N = int(input())
    triangle = []
    for i in range(N):
        temp = input().split(' ')
        triangle.append([int(x) for x in temp])
    for i in range(N-1, 0, -1):
        for j in range(0, i):
            triangle[i-1][j] += max(triangle[i][j], triangle[i][j+1])
    print(triangle[0][0])


solution()

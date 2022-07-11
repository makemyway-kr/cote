import sys
N = int(sys.stdin.readline().rstrip())
M = int(sys.stdin.readline().rstrip())
connections = [[0 for c in range(N+1)] for d in range(N+1)]
visitied = [1, ]
answer = 0
for i in range(M):
    a, b = map(int, sys.stdin.readline().rstrip().split(' '))
    connections[a][b] = 1
    connections[b][a] = 1


def dfs(curr):
    global connections, visitied, answer
    for c in range(N+1):
        if connections[curr][c] == 1 and c not in visitied:
            answer += 1
            visitied.append(c)
            dfs(c)


dfs(1)
print(answer)

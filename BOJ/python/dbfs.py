import sys
N, M, V = map(int, sys.stdin.readline().rstrip().split(' '))
connections = [[0 for c in range(N+1)] for d in range(N+1)]
dvisitied = [V]
bvisitied = []
tovisit = set()
bqueue = [V, ]


def dfs(curr):
    global connections, dvisitied
    for c in range(N+1):
        if connections[curr][c] == 1 and c not in dvisitied:
            dvisitied.append(c)
            dfs(c)


def bfs():
    global connections, bvisitied, bqueue, V
    while len(bqueue)!=0:
        curr = bqueue.pop(0)
        bvisitied.append(curr)
        for c in range(N+1):
            if connections[curr][c] == 1 and c not in bvisitied and c not in bqueue:
                bqueue.append(c)
    temp = ''
    if len(tovisit) == 0:
        print(V)
        return
    for v in bvisitied:
        temp += str(v)+' '
    print(temp[0:-1])


for i in range(M):
    a, b = map(int, sys.stdin.readline().rstrip().split(' '))
    tovisit.add(a)
    tovisit.add(b)
    connections[a][b] = 1
    connections[b][a] = 1
dfs(V)
temp = ''
for v in dvisitied:
    temp += str(v) + ' '
print(temp[0:-1])
bfs()

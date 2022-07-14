from operator import indexOf
import sys

N,M = map(int,sys.stdin.readline().rstrip().split())
result = [[0 for r in range(M)] for c in range(N)]
starter = [0,0]
nonreachable = []
visitied = []
def visitor(r,c,d):
    global result
    if r<0 or c<0 or r>=M or c>=N:
        return
    elif [r,c] in nonreachable:
        visitied.append([r,c])
        return
    elif [r,c] not in visitied:
        visitied.append([r,c])
        result[r][c] = d
        visitor(r+1,c,d+1)
        visitor(r,c+1,d+1)
        visitor(r-1,c,d+1)
        visitor(r,c-1,d+1)

for r in range(M):
    temp = [int(x) for x in sys.stdin.readline().rstrip().split()]
    if 2 in temp:
        tc = indexOf(temp,2)
        starter = [r,tc]
    if 0 in temp:
        for i in range(N):
            if temp[i] == 0:
                nonreachable.append([r,i])
visitor(starter[0],starter[1],0)
print(result)
def solution(n, start, end, roads, traps):
    answer = 0
    curr = start
    links = [ [0 for x in range(n)] for c in range( n )]
    for r in roads: #가중치와 인접 에지의 트랩 발동횟수를 링크 행렬에 표시
        links[r[0]][r[1]] = [r[2],0]
    trapCount = [[t,0] for t in traps]
    visitied = [ 0 for x in range(n) ]
    distance = [9999 for x in range(n)]
    while curr != end:
        min = []
        if curr in traps:
            for l in links[curr]:
                if (l[1]+1) % 2 == 0: #if road hasn't changed
                    for d in range(n):
                        if l[0] < distance[d]:
                            distance[d] = l[0]
    
    return answer

print(solution(3,1,3,[[1, 2, 2], [3, 2, 3]],[2]))
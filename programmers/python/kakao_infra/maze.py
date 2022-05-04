def solution(n, start, end, roads, traps):
    answer = 0
    curr = start
    trapRoads = [ [x[1],x[0],x[2] ] for x in roads ]
    trapCount = 0
    visitied = [ 0 for x in range(n) ]
    counter = 0
    
    return answer

print(solution(3,1,3,[[1, 2, 2], [3, 2, 3]],[2]))
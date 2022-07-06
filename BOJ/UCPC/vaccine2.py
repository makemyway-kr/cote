before = []
after = []


def dfs(row, col):
    queue = [[row, col]]
    print(row, col)
    global before
    global after
    for r in range(row, len(before)):
        for c in range(col, len(before[0])):
            if before[r][c] == before[row][col] and ([r-1, c] in queue or
                                                     [r, c-1] in queue):
                before[r][c] = after[row][col]
                queue.append([r, c])
            else:
                break
    print(queue)


def solution():
    rowAndCol = input().split(' ')
    row = int(rowAndCol[0])
    col = int(rowAndCol[1])
    global before
    global after
    answer = 'YES'
    dfsCount = 0
    for r in range(row):
        temp = input()
        temp = temp.split(' ')
        before.append([int(i) for i in temp])
    for r in range(row):
        temp = input()
        temp = temp.split(' ')
        after.append([int(i) for i in temp])
    if before == after:
        print(answer)
        return answer
    for r in range(row):
        for c in range(col):
            if before[r][c] != after[r][c]:
                dfs(r, c)
                dfsCount += 1
        if dfsCount > 0:
            break
    if before != after:
        answer = 'NO'
    print(answer)


solution()

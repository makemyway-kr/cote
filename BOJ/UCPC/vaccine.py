def solution():
    rowAndCol = input().split(' ')
    row = int(rowAndCol[0])
    col = int(rowAndCol[1])
    before = []
    after = []
    answer = 'YES'
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
    diffs = []
    for r in range(row):
        for c in range(col):
            if before[r][c] != after[r][c]:
                if len(diffs) == 0:
                    diffs.append(before[r][c])
                    diffs.append([[r, c]])
                else:
                    if ([r-1, c] in diffs[1]) or ([r, c-1] in diffs[1]):
                        diffs[1].append([r, c])
                    else:
                        answer = 'NO'
                        break
            elif len(diffs) != 0:
                if before[r][c] == after[r][c] and ([r-1, c] in diffs[1] or [r, c-1] in diffs[1])\
                        and before[r][c] == diffs[0]:
                    answer = 'NO'
                    break
        if answer == 'NO':
            break
    print(answer)


solution()

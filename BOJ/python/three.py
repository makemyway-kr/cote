N = int(input())

numb = [0, 1, 2]
answer = 0


def makeNumber(num, s):
    global N, answer
    if len(num) == N and s % 3 == 0:
        answer += 1
    elif len(num) == N:
        return
    else:
        makeNumber(num+'0', s)
        makeNumber(num+'1', s+1)
        makeNumber(num+'2', s+2)


if N == 1:
    print(0)
else:
    makeNumber('1', 1)
    makeNumber('2', 2)
    print(answer)

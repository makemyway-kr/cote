#프로그래머스 정수삼각형 문제 https://programmers.co.kr/learn/courses/30/lessons/43105?language=python3
finalcals=[]
def dp(triangle,currow,currcol,curr):
    if(currow!=len(triangle)-1):
        dp(triangle,currow+1,currcol,curr+triangle[currow+1][currcol])
        dp(triangle,currow+1,currcol+1,curr+triangle[currow+1][currcol+1])
    else:
        finalcals.append(curr)
def solution(triangle):
    #각 숫자의 행번호는 +1 이고 열 번호가 같은것, 또는 1 큰것으로 이동 가능함. [1][0]이면 [2][0] 또는 [2][1]로 이동가능
    dp(triangle,0,0,triangle[0][0])
    return sorted(finalcals,reverse=True)[0]
print(solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]))
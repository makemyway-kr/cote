#프로그래머스 정수삼각형 문제 https://programmers.co.kr/learn/courses/30/lessons/43105?language=python3
def dp(triangle,currow,currcol,curr):
    result=[]
    result.append([curr+triangle[currow+1][currcol],currcol])
    result.append([curr+triangle[currow+1][currcol+1],currcol+1])
    return result
def solution(triangle):
    answer = 0
    #각 숫자의 행번호는 +1 이고 열 번호가 같은것, 또는 1 큰것으로 이동 가능함. [1][0]이면 [2][0] 또는 [2][1]로 이동가능
    calcul=[[]for row in range(len(triangle))]#검색결과를 [값,열]의 형태로 넣음.
    calcul[0].append([triangle[0][0],0])
    row=0
    while row<len(triangle)-1:#열을 증가시키며 각 경우의수를 계산함.
        for c in calcul[row]:
            dpresult=dp(triangle,row,c[1],c[0])
            for d in dpresult:
                calcul[row+1].append(d)
        row+=1
    temp=sorted(calcul[len(triangle)-1],key=lambda x:x[0],reverse=True)#값기준 내림차순 정렬
    answer=temp[0][0]
    return answer
print(solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]))
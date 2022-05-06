#프로그래머스 정수삼각형 문제 https://programmers.co.kr/learn/courses/30/lessons/43105?language=python3
#삼각형을 잘게 잘라서 행이 1개, 2개, 3개,4개....n개까지 구해나간다는 생각으로.
def solution(triangle):
    if len(triangle)>2:
        triangle[1][0]+=triangle[0][0]
        triangle[1][1]+=triangle[0][0]
        if(len(triangle)>3):
            for row in range(2,len(triangle)):
                for col in range(len(triangle[row])):
                    if col==0 or col==len(triangle[row])-1:
                        if col==0:
                            triangle[row][col]+=triangle[row-1][col]
                        else:
                            triangle[row][col]+=triangle[row-1][col-1]
                    else:
                        triangle[row][col]+=max(triangle[row-1][col-1],triangle[row-1][col])
    return max(triangle[len(triangle)-1])
print(solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]))
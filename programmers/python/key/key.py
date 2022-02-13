#https://programmers.co.kr/learn/courses/30/lessons/60059 level 3문제
def solution(key,lock):
    answer = True
    padding = len(key-1)
    key_matcher = [[1 for col in range (len(lock) + padding)] for row in range (len(lock) + padding)]#키의 변 길이 -1만큼 패딩을 넣음.
    for row in range(len(lock)):
        for col in range(len(lock)):
            if lock[row,col]==0:
                key_matcher[row+padding,col+padding]=0
    zero_zero_key=[0,0]
    key_end=[len(key)-1,len(key),-1]
    return answer
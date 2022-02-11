#https://programmers.co.kr/learn/courses/30/lessons/60059 level 3문제
def solution(key,lock):
    answer = True
    panding = len(key-1)
    key_matcher = [[1 for col in range (len(lock) + panding)] for row in range (len(lock) + panding)]
    return answer
from multiprocessing import Process
#먼저 p들 다 찾고 그 중에 거리 2 이하인 애들 대상으로만 검사
#https://programmers.co.kr/learn/courses/30/lessons/81302
def search_and_catch(place):
    checked = []
    plist = []
    for r in range(5):
        for c in range(5):
            if place[r][c] == 'p':
                plist.append([r,c])

        
def solution(places):
    answer = [1 for i in range(len(places))]
    
    return answer
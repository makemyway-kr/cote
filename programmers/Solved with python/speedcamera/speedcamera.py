#프로그래머스 단속카메라문제 https://programmers.co.kr/learn/courses/30/lessons/42884?language=python3
def solution(routes):
    routes.sort(key=lambda x:x[1])#진출지점이 빠른 순서대로 정렬.
    cameras=[]
    cameras.append(routes[0][1])#첫번째 진출지점에 카메라를 설치
    for r in routes:
        check=False
        for c in cameras:
            if c>=r[0] and c<=r[1]:#진입지점과 진출지점의 사이에 카메라가 존재하면
                check=True
                break
        if check==False:
            cameras.append(r[1])
    answer=len(cameras)
    return answer
print(solution([[-20,15], [-14,-5], [-18,-13], [-5,-3]]))
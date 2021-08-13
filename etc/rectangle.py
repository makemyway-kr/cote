#프로그래머스 연습문제
def solution(v):
    answer = []
    RE=v[0][0]
    LE=v[0][0]
    UE=v[0][1]
    DE=v[0][1]
    for point in v:
        if point[0]<LE:
            LE=point[0]
        elif point[0]>RE:
            RE=point[0]
        if point[1]>UE:
            UE=point[1]
        elif point[1]<DE:
            DE=point[1]
    if [RE,UE] not in v:
        answer=[RE,UE]
    elif [RE,DE] not in v:
        answer=[RE,DE]
    elif [LE,UE] not in v:
        answer=[LE,UE]
    elif [LE,DE] not in v:
        answer=[LE,DE]
    return answer
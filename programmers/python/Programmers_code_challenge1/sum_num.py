def solution(absolutes, signs):#부호와 숫자를 더해서 나온 값을 return하기만 하면 됨.
    answer = 0
    length=len(absolutes)
    for i in range(length):
        if signs[i]==True:
            answer+=absolutes[i]
        elif signs[i]==False:
            answer-=absolutes[i]
    return answer
def solution(N, number):
    answer = -1
    numbers=[]
    if N==number:
        answer=1
    else:
        temp=N
        numbers.append([N])
        for i in range(1,8):
            temp=(temp*10)+N
            numbers.append([temp])
        for list in numbers:
            if number in list:
                answer=numbers.index(list)+1
        else:
            for usedN in range(2,9):#쓰일 N숫자의 수를 통제함.
                for i in range(1,usedN):
                    l=usedN-i#N의 횟수 합이 usedN과 일치하도록.
                    for left in numbers[i-1]:
                        for right in numbers[l-1]:
                            if left+right not in numbers[usedN-1]:
                                numbers[usedN-1].append(left+right)
                            if left*right not in numbers[usedN-1]:
                                numbers[usedN-1].append(left*right)
                            if right>0 and left//right>=1 and left//right not in numbers[usedN-1]:
                                numbers[usedN-1].append(left//right)
                            if left-right>0 and left-right not in numbers[usedN-1]:
                                numbers[usedN-1].append(left-right)
            for list in numbers:
                if number in list:
                    answer=numbers.index(list)+1
                    break
    return answer
print(solution(5,12))
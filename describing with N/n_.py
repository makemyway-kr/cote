import math
def solution(N, number):
    answer = 0
    if N==number:
        answer=1
    else:
        numbers_to_use=[]
        numbers_to_use.append([N])
        for i in range(1,8):
            temp_array=[]
            temp=N
            for k in range(i):
                temp=(temp*10)+N #기본 숫자 넣어둠
            temp_array.append(temp)
            numbers_to_use.append(temp_array)
        if N in numbers_to_use:
            answer=len(str(N));
        else:
            for i in range(2,8):
                for k in range(1,i):
                    index1=i-k-1
                    index2=k-1
                    for nu1 in numbers_to_use[index1]:
                        for nu2 in numbers_to_use[index2]:
                            numbers_to_use[i-1].append(nu1+nu2)
                            numbers_to_use[i-1].append(nu1*nu2)
                            if nu1-nu2>=0:
                                numbers_to_use[i-1].append(nu1-nu2)
                            if nu1!=0 and nu2!=0 and nu1/nu2>=0:
                                numbers_to_use[i-1].append(math.floor(nu1/nu2))
                    if N in numbers_to_use[i-1]:
                        answer=i
                        print(numbers_to_use[i-1])
                        break
    return answer
print(solution(5,12))
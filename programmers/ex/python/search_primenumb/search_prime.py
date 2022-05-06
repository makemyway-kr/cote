import math
from itertools import permutations
def check_if_prime(num):
    ret=True
    if(num<2):
        return False
    else:
        for i in range(2,int(math.sqrt(num)+1)):
            if(num%i)==0:
                ret=False
                break
        return ret
    '''어떤 수가 a라는 수의 배수, 즉 a가 어떤 수 X의 약수이면 x/a도 X의 약수이고, 이 말은
    x가 소수가 아니라는 것이므로 굳이 x전의 모든 수를 검사하지않고 제곱근까지만 검사하면 됨'''
def solution(numbers):
    alist=[]
    length=len(numbers)
    for i in range(1,length+1):
        '''조합 갯수 반복문'''
        perofnumbers=list(map(''.join,permutations(numbers,i)))
        for k in perofnumbers:
            if check_if_prime(int(k))==True:
                alist.append(int(k))
    anslist=list(set(alist))
    return len(anslist)
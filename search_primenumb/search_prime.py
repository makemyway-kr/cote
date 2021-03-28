def check_if_prime(num):
    if(num<2):
        return False
    else:'''어떤 수가 a라는 수의 배수, 즉 a가 어떤 수 X의 약수이면 x/a도 X의 약수이고, 이 말은
    x가 소수가 아니라는 것이므로 굳이 x전의 모든 수를 검사하지않고 제곱근까지만 검사하면 됨'''
    


def solution(numbers):
    length=len(numbers)
    even={}
    odd={}

    for i in range (length): '''dividing odd numbers and even numbers b/c 
    even numbers cannot be the last digit of prime number'''
        if int(numbers[i])%2==0:
            even.append(numbers[i])
        else:
            odd.append(numbers[i])
    
    return answer
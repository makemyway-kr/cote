def solution(numbers):
    numbers=list(map(str,numbers))
    #최대 세자리수 이므로, 모두 최소 3자리수 이상으로 만들어 둔 뒤 ascii코드를 이용해 비교및 정렬한다.
    numbers.sort(key=lambda x: x*3,reverse=True)
    '''lambda x: x*3이란, f(x)=xxx(x를 3번 반복함)과 같다. 이렇게 하면 한자리 수도 최소 3자리 수가 되어, 두자리, 세자리수와 문자열 비교가 가능해진다.
    이렇게하면, 예를 들어 6과 63이 있을떄, 663이 큰지, 636이 큰지 일일이 비교할 필요없이 666과 636363을 비교해서, 6을 앞에 두고 63을 뒤에 두어
    663순으로 정렬한다.'''
    answers=""
    if numbers[0]=="0":
        return "0"
    for i in numbers:
        answers=answers+i;
    return answers
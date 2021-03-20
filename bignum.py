def solution(numbers):
    
    answer = ''
    while len(numbers)!=0:
        temp=10
        cur=0
        rnum=0
        for num in numbers:
            cur=num%10
            if cur<temp:
                temp=cur
                rnum=num
        answer=str(rnum)+answer
        numbers.remove(rnum)

        
    return answer
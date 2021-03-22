def comparing(a, b):
    if str(a)+str(b)>=str(b)+str(a):
        return True
    else:
        return False
def solution(numbers):
    
    answer = ''
   
    for i in range(len(numbers)-1,0,-1):

        for j in range(0,i):
            if comparing(numbers[j],numbers[j+1])==False:
                temp=0
                temp=numbers[j+1]
                numbers[j+1]=numbers[j]
                numbers[j]=temp

    if(numbers[0]=='0'):
        return 0

    numbers=map(str,numbers)

    for i in numbers:
        answer=answer+i
    return answer
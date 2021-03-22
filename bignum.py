def comparing(a, b):
    a=str(a)
    b=str(b)
    if a+b>=b+a:
        return True
    else:
        return False
def solution(numbers):
    
    answer = ''
   
    for i in range(len(numbers)-1):
        j=i+1
        for j in range(len(numbers)):
            if comparing(i,numbers[j])==False:
                temp=0
                temp=numbers[j]
                numbers[j]=numbers[i]
                numbers[i]=temp
    if(numbers[0]=='0'):
        return 0

    numbers=map(str,numbers)

    for i in numbers:
        answer=answer+i
    return answer
   
        
  
   
        
    
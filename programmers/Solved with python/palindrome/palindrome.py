def solution(s):
    answer = 0
    for l in range(len(s),0,-1):#iteration with length
        print('iteration',l)
        head=0
        tail=head+l-1
        while(tail<len(s)):
            h=head
            t=tail
            p=True
            while h<=t:
                if s[h]!=s[t]:
                    p=False
                    break
                h-=1
                t-=1
            if p==True:
                answer=l
                break
            head+=1
            tail=head+l-1
        if answer!=0:
            break
    return answer
print(solution('abccba'))
def solution(begin, target, words):
    answer = 0
    if target not in words:
        return 0
    else:
        count_for_changing=0
        for i in range(len(target)):
            if begin[i]!=target[i]:
                count_for_changing+=1
        for i in words:
            temp=0
            for k in range(len(i)):
                if begin[k]!=i[k]:
                    temp+=1
            if temp==1 and count_for_changing>1:#알파벳이 하나 다르면
                begin=i
                count_for_changing=0
                for i in range(len(target)):
                    if begin[i]!=target[i]:
                        count_for_changing+=1
                answer+=1
            elif count_for_changing==1:
                answer+=1
                break
        return answer
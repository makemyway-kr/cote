def solution(gems):
    answer=[]
    gemlist=set(gems)
    shortestlength=100001
    start=0
    end=0
    currentgems={}
    while end<len(gems):
        if gems[end] not in currentgems:
            currentgems[gems[end]]=1
        else:
            currentgems[gems[end]]+=1
        end+=1
        if len(currentgems)==len(gemlist):#만약 현재 상태에서 모든 보석이 담겨있으면 앞을 줄여나가면서 가장 작은 보석개수를 구해봄
            while start<end:
                if currentgems[gems[start]]>1:#가장 앞 지점(포인트)가 가리키는 보석이 두개이상 존재한다면 하나 빼고 앞 포인트를 뒤로 당김.
                    currentgems[gems[start]]-=1
                    start+=1
                elif shortestlength>end-start: #더이상 앞 포인터를 뒤로 옮기면 모든 보석의 종류가 포함되지 않음. 근데 최소길이보다 작은 길이임.
                    shortestlength=end-start
                    answer=[start+1,end]
                    break
                else:#최소길이가 아님.
                    break
    return answer
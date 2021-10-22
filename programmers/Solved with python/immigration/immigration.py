def solution(n, times):
    answer = []
    times.sort(key=lambda x : x)
    right=n*times[len(times)-1]#right side is the maximum time needed when the office needing most time does all jobs
    left=1
    mid=right+left//2
    if len(times)==n:
        answer.append(max(times))
    elif n==1:
        answer.append(min(times))
    else:
        while(left<=right):
            mid=(right+left)//2
            handled=0#people who finished immigration
            for t in times: #people will go to immigration officer who needs less time first
                handled+=mid//t
                if handled>=n:
                    break #if people finished immigration exceeds n or same, finish for loop
            if handled>n:
                right=mid-1
                answer.append(mid)
            elif handled<n:
                left=mid+1
            else:
                answer.append(mid)
                right=mid-1
    return min(answer)
print(solution(3,[7,10]))
def solution(s):
    answer = -1
    for start in range(len(s)-2):
        if s[start] == s[start+1] == s[start+2]:
            if int(s[start:start+3]) > answer:
                answer = int(s[start:start+3])
    return answer
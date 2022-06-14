def solution(survey, choices):
    answer = ''
    characs = {"R": 0 , "T":0, "C" : 0 , "F" : 0,  "J" : 0, "M" : 0 , "A": 0 , "N": 0 }
    for i in range(len(survey)):
        if choices[i] < 4:
            characs[survey[i][0]] += (4-choices[i])
        elif choices[i] > 4:
            characs[survey[i][1]] += (choices[i]-4)
    keys = list(characs.keys())
    for i in range(0,len(keys)-1 , 2):
        if characs[keys[i]] > characs[keys[i+1]]:
            answer += keys[i]
        elif characs[keys[i]] == characs[keys[i+1]]:
            answer += keys[i]
        else:
            answer += keys[i+1]
    return answer
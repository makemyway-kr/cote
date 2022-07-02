def solution():
    inputString = input()
    inputString = inputString.split(' ')
    timeNeed = int(inputString[0])
    d = float(float(inputString[1])/100)
    k = float(float(inputString[2])/100)
    probs = [d]
    temp = d
    max_hundred = 1
    while temp < 1:
        temp += (temp*k)
        probs.append(temp)
        max_hundred += 1
    answer = 0.0
    i = 1
    probs[-1] = 1.0
    while i <= max_hundred:
        temp = timeNeed * i
        for j in range(i):
            if j == i-1:
                temp *= probs[j]
            else:
                temp *= (1-probs[j])
        answer += temp
        i += 1
    print(answer)


solution()

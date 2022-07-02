def solution():
    inputNum = input()
    startNum = 0
    finNum = 0
    for i in range(1, len(inputNum)):
        startNumPredicted = ''
        startNumPredicted += inputNum[0:i]
        temp = int(startNumPredicted)
        while len(startNumPredicted) < len(inputNum):
            temp += 1
            startNumPredicted += str(temp)
        if startNumPredicted == inputNum:
            startNum = int(inputNum[0:i])
            finNum = int(temp)
            break
    if startNum == 0:
        startNum = int(inputNum)
        finNum = int(inputNum)
    print(startNum)
    print(finNum)


solution()

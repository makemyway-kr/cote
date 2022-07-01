import math


def solution():
    inputNum = input()
    startNum = 0
    finNum = 0
    for i in range(1, (math.floor(len(inputNum)/2)) + 1):
        if int(inputNum[0:i]) + 1 == int(inputNum[i:i+i]) \
                or (int(inputNum[0:i]) + 1 == int(inputNum[i:i+i+1])
                    and inputNum[i] != '0'):
            startNum = int(inputNum[0:i])
            break
    if startNum == 0:
        startNum = int(inputNum)
        finNum = int(inputNum)
        print(startNum)
        print(finNum)
    else:
        length = len(str(startNum))
        pointer = 0
        while pointer + length <= len(inputNum):
            if pointer + length == len(inputNum):
                finNum = int(inputNum[pointer:pointer+length])
                pointer += length
            elif int(inputNum[pointer:pointer+length]) + 1 == 10:
                pointer += length
                length = 2
            elif int(inputNum[pointer:pointer+length]) + 1 == 100:
                pointer = pointer + length
                length = 3
            else:
                pointer += length
        print(startNum)
        print(finNum)


solution()

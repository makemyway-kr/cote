from itertools import combinations
vowel = ['a','e','i','o','u']
def solution():
    temp = input().split(' ')
    L = int(temp[0])
    C = int(temp[1])
    alphabets = [ i for i in input().split(' ') ]
    alphabets.sort()
    pws = combinations(alphabets,L)
    for p in pws:
        vcount = 0
        nvcount = 0
        temp = ''
        for a in p:
            if a in vowel:
                vcount += 1
            else:
                nvcount += 1
            temp += a
        if vcount >= 1 and nvcount >= 2:
            print(temp)
solution()
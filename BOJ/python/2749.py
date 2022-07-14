def fibo_not_recursive(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    a = 0
    b = 1
    curr = 2
    while True:
        temp = b
        b = (a+b)%1000000
        a = temp
        if curr == n:
            break
        curr += 1
    return b
N = int(input())
print(fibo_not_recursive(N%1500000))
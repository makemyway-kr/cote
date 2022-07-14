def fibo(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibo(n-1) + fibo(n-2)
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
        b = a+b
        a = temp
        if curr == n:
            break
        curr += 1
    return b
print(fibo_not_recursive(int(input())))
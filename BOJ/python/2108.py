import sys

N = int(sys.stdin.readline().rstrip())
numbers = []
numbers_count = {}
max_count = 1
for i in range(N):
    temp = int(sys.stdin.readline().rstrip())
    numbers.append(temp)
    if temp in numbers_count.keys():
        numbers_count[temp] += 1
        if numbers_count[temp] > max_count:
            max_count = numbers_count[temp]
    else:
        numbers_count[temp] = 1
numbers.sort()
print(round(sum(numbers)/N))
print(numbers[round((len(numbers)-1)/2)])
maxes = []
for k in numbers_count.keys():
    if numbers_count[k] == max_count:
        maxes.append(k)
maxes.sort()
if len(maxes) > 1:
    print(maxes[1])
else:
    print(maxes[0])
print(numbers[-1]-numbers[0])

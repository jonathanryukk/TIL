import copy

result = []

a = int(input())
max_list = 0

result = []
for i in range(101):
    arr = [a, i]
    x = 0
    while True:
        tmp = arr[x] - arr[x + 1]
        if tmp >= 0:
            arr.append(tmp)
        else:
            if max_list < len(arr):
                max_list = i

            break
        x += 1

print(result)

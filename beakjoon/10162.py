a = int(input())
arr = [300, 60, 10]

result = [0, 0, 0]

for i in range(3):
    if a >= arr[i]:
        result[i] += a // arr[i]
        a = a % arr[i]
result = ' '.join(map(str, result))

if a == 0:
    print(result)
else:
    print(-1)

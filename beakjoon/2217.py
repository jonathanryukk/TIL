N = int(input())
arr = []
for i in range(N):
    arr.append(int(input()))

arr.sort(reverse=True)

result= []

for i in range(N):
    result.append(arr[i]*(i+1))

print(max(result))
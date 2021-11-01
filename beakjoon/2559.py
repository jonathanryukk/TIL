n, k = map(int, input().split())
arr = list(map(int, input().split()))

tmp = sum(arr[:k])
res = [tmp]

for i in range(0, len(arr) - k):
    tmp = tmp - arr[i] + arr[i + k]
    res.append(tmp)

print(max(res))

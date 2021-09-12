N = int(input())
lens = list(map(int, input().split()))
price = list(map(int, input().split()))
ST = []
result = 0
ST.append(price[0])
for i in range(1, N - 1):
    if ST[-1] > price[i]:
        result += ST[-1] * lens[i - 1]
        ST.append(price[i])
    else:
        result += ST[-1] * lens[i - 1]

result += ST[-1] * (lens[-1])

print(result)
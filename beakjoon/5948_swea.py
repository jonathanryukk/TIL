t = int(input())
for tc in range(1, t + 1):
    arr = list(map(int, input().split()))
    arr.sort()
    list1 = []
    for i in arr:
        for j in arr:
            if i == j:
                continue
            for z in arr:
                if i == z or j == z:
                    continue
                list1.append(i + j + z)
    list1 = list(set(list1))
    list1.sort()
    print(f'#{tc} {list1[-5]}')

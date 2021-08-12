t = int(input())

for num in range(1,t+1):
    a = int(input())
    list_a = list(map(int, input().split()))

    for i in range(1, len(list_a)):
        for j in range(0, len(list_a)-1):
            if list_a[j] > list_a[j+1]:
                list_a[j], list_a[j+1] = list_a[j+1], list_a[j]

    print(*list_a)
    result = ' '.join(map(str, list_a))
    print(f'#{num} {result}')
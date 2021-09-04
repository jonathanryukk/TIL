t = int(input())
for tc in range(1, t + 1):
    a = list(input())
    N = int(input())
    list1 = [''] * (len(a) + 1)
    arr = list(map(int, input().split()))

    for i in arr:
        list1[i] += '-'

    print(f'#{tc}', end=' ')
    for i in range(len(a)):
        print(list1[i], end='')
        print(a[i], end='')
    if list1[-1]:
        print(list1[-1], end='')
    print()

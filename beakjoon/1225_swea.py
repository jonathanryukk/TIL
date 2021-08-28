for tc in range(1, 11):
    num = int(input())
    arr = list(map(int, input().split()))
    r = 1

    while r == 1:
        for i in range(1, 6):
            arr.append(arr.pop(0) - i)
            if arr[-1] <= 0:
                arr[-1] = 0
                r = 0
                break

    result = " ".join([str(_) for _ in arr])
    print(f'#{num} {result}')

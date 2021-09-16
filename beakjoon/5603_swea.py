t = int(input())

for tc in range(1, t + 1):
    list1 = []
    N = int(input())
    for i in range(N):
        list1.append(int(input()))

    result = sum(list1) // len(list1)
    sum1 = 0
    for i in list1:
        if i >= result:
            sum1 += (i - result)
        else:
            sum1 += (result - i)

    print(f'#{tc} {sum1 // 2}')
    # result = sum(list1) // len(list1)
    # cnt = 0
    # while True:
    #     list1.sort()
    #     if list1[0] == result and list1[-1] == result:
    #         break
    #     else:
    #         list1[0] += 1
    #         list1[-1] -= 1
    #     cnt += 1
    # print(f'#{tc} {cnt}')

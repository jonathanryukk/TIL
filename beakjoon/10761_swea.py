TC = int(input())
for tc in range(1, TC + 1):
    ARR = list(input().split())
    arrB = []
    arrO = []
    for i in range(int(ARR[0])):
        if ARR[2 * i + 1] == 'B':
            arrB.append(int(ARR[2 * i + 2]))
        elif ARR[2 * i + 1] == 'O':
            arrO.append(int(ARR[2 * i + 2]))
    push_ARR = 1
    pos_B = 1
    pos_O = 1
    cnt = 0

    while arrB or arrO:
        len_ARR = len(arrO) + len(arrB)
        if arrB:
            if pos_B < arrB[0]:
                pos_B += 1
            elif pos_B > arrB[0]:
                pos_B -= 1
            elif pos_B == arrB[0] and ARR[push_ARR] == 'B':
                arrB.pop(0)

        if arrO:
            if pos_O < arrO[0]:
                pos_O += 1
            elif pos_O > arrO[0]:
                pos_O -= 1
            elif pos_O == arrO[0] and ARR[push_ARR] == 'O':
                arrO.pop(0)
        new_len_ARR = len(arrO) + len(arrB)
        if len_ARR != new_len_ARR:
            push_ARR += 2

        cnt += 1

    print(f'#{tc} {cnt}')

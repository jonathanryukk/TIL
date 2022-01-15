for i in range(3):
    str = input().split()
    cnt = 0
    for i in range(4):
        if str[i] == '0':
            cnt += 1

    if cnt == 0:
        print('E')

    elif cnt == 1:
        print('A')

    elif cnt == 2:
        print('B')

    elif cnt == 3:
        print('C')

    else:
        print('D')

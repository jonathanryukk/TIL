t = int(input())

for tc in range(1, t + 1):
    arr = input()
    S = []
    D = []
    H = []
    C = []
    result = 0
    for i in range(len(arr)):
        if arr[i] == 'S':
            if int(arr[i + 1] + arr[i + 2]) in S:
                result = 'ERROR'
                break
            S.append(int(arr[i + 1] + arr[i + 2]))
        if arr[i] == 'D':
            if int(arr[i + 1] + arr[i + 2]) in D:
                result = 'ERROR'
                break
            D.append(int(arr[i + 1] + arr[i + 2]))
        if arr[i] == 'H':
            if int(arr[i + 1] + arr[i + 2]) in H:
                result = 'ERROR'
                break
            H.append(int(arr[i + 1] + arr[i + 2]))
        if arr[i] == 'C':
            if int(arr[i + 1] + arr[i + 2]) in C:
                result = 'ERROR'
                break
            C.append(int(arr[i + 1] + arr[i + 2]))

    Slen = 13 - len(S)
    Dlen = 13 - len(D)
    Hlen = 13 - len(H)
    Clen = 13 - len(C)

    if result == 'ERROR':
        print(f'#{tc} {result}')
    else:
        print(f'#{tc} {Slen} {Dlen} {Hlen} {Clen}')

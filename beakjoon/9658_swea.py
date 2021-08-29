t = int(input())

for tc in range(1, t + 1):
    A = int(input())
    A_list = list(map(int, str(A)))
    cnt = A / (10**(len(A_list)-1))
    result = round(cnt,1)

    if A_list[0] ==9 and A_list[1] >=5:
        print(f'#{tc} {result}*10^{len(A_list)}')
    else:
        print(f'#{tc} {result}*10^{len(A_list)-1}')
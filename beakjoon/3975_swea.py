t = int(input())
lst = []
for tc in range(1, t + 1):
    lst.append(list(map(int,input().split())))

for tc in range(t):
    rate_a = lst[tc][0] / lst[tc][1]
    rate_b = lst[tc][2] / lst[tc][3]

    if rate_a == rate_b:
        print(f'#{tc + 1} DRAW')
    elif rate_a > rate_b:
        print(f'#{tc + 1} ALICE')
    else:
        print(f'#{tc + 1} BOB')

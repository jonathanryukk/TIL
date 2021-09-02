t = int(input())

for tc in range(1, t + 1):
    a = list(input())
    a.sort()
    ST = []

    for i in range(len(a)):
        if len(ST) == 0:
            ST.append((a[i]))
        elif a[i] != ST[-1]:
            ST.append(a[i])
        else:
            ST.pop(-1)

    if len(ST) == 0:
        print(f'#{tc} Good')
    else:
        result = ''.join(ST)
        print(f'#{tc} {result}')

t = int(input())

for tc in range(1, t + 1):
    L, U, X = map(int, input().split())
    if X > U:
        print(f'#{tc} -1')
    elif L > X:
        print(f'#{tc} {L-X}')
    else:
        print(f'#{tc} 0')

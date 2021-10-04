t = int(input())

for tc in range(1,t+1):
    D,L,N = map(int,input().split())
    damage = 0
    for i in range(N):
        damage += D+D*i*L/100
    print(f'#{tc} {int(damage)}')
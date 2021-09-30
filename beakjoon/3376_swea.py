t = int(input())
padoban = [1,1,1]

for i in range(3,101):
    padoban.append(padoban[i-2]+padoban[i-3])

for tc in range(1,t+1):
    n = int(input())
    print(f'#{tc} {padoban[n-1]}')
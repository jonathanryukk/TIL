t = int(input())

for i in range(1,t+1):
    P, Q, R, S, W = map(int,input().split())

    a = P*W
    if R > W:
        b = Q
    else:
        b = Q +(W-R)*S
    
    if a>b:
        print(f'#{i} {b}')
    else:
        print(f'#{i} {a}')
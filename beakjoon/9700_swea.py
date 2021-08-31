t = int(input())

for tc in range(1,t+1):
    p,q = map(float, input().split())

    s1 = (1-p)*q
    s2 = (p)*(1-q)

    if s1<s2:
        result = 'YES'
    else:
        result = 'NO'
    print(f'#{tc} {result}')
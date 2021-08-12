cnt=int(input())
for i in range(cnt):
    Mi, Di, Mj, Dj = map(int, input().split())
    date_31 = [1, 3, 5, 7, 8, 10, 12]
    date_30 = [4, 6, 9, 11]
    Mi_date = 0
    Mj_date = 0
    for k in range(1, Mi+1):
        if k in date_31:
            Mi_date += 31
        elif k in date_30:
            Mi_date += 30
        else:
            Mi_date += 28
    for s in range(1, Mj+1):
        if s in date_31:
            Mj_date += 31
        elif s in date_30:
            Mj_date += 30
        else:
            Mj_date += 28
    Mi_date += Di
    Mj_date += Dj        
    print(f'#{i+1} {Mj_date - Mi_date + 1}')
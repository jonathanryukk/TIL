t = int(input())

for num in range(1,t+1):
    h, m, h1, m1 = map(int, input().split())
    a_h = 0
    a_m = 0
    if m + m1 > 60:
        a_m = m + m1 -60 
        h += 1
    else: 
        a_m = m + m1
    
    if h + h1 > 12:
        a_h = h + h1 - 12
    else:
        a_h = h + h1 

    print(f'#{num} {a_h} {a_m}')
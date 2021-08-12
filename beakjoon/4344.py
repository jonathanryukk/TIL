t = int(input())
for i in range(t):
    a = list(map(int, input().split()))
    avg = sum(a[1:])/a[0]
    cnt = 0
    for j in a[1:]:
        if j > avg:
            cnt += 1
    result = (cnt/a[0])*100
    print('%.3f' %result +'%')


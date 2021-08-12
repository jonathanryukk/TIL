
t = int(input())

for i in range(1,t+1):
    A, B = map(int,input().split())
    list_a = list(map(int,input().split()))
    list_b = list(map(int,input().split()))
    sum = 0
    if A > B:
        for a in range(A-B+1):
            tmp = 0
            for b in range(B):
                tmp = tmp + (list_a[b+a] * list_b[b])
            if tmp > sum: 
                sum = tmp
        print(f'#{i} {sum}')        
    else:
        for c in range(B-A+1):
            tmp1 = 0
            for d in range(A):
                tmp1 = tmp1 + (list_b[d+c] * list_a[d])
            if tmp1 > sum:
                sum = tmp1
        print(f'#{i} {sum}')


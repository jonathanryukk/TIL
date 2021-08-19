import sys
sys.stdin = open('input.txt')

t = int(input())
for num in range(1,t+1):
    result = ''
    N = int(input())

    for i in range(N):
        a,b = input().split()
        result += a*int(b)
    print(f'#{num}')
    cnt = 1
    for i in result:
        print(i,end='') 
        if cnt%10 == 0:
            print('')
        cnt += 1
    print()


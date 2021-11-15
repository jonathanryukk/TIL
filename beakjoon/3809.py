import sys 
sys.stdin = open('input.txt')

t = int(input())

for tc in range(1,t+1):
    N = int(input())
    a= ''
    while True:
        a += ''.join(map(str,input().split()))
        if len(a) ==N:
            break
    cnt = 0
    while True:
        if str(cnt) not in a:
            break
        cnt+=1

    print(f'#{tc} {cnt}')


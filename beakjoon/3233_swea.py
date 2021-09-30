t = int(input())

for tc in range(1,t+1):
    A,B = map(int,input().split())

    print(f'#{tc} {(A//B)**2}')
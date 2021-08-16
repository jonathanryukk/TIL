import sys
sys.stdin = open('input.txt')

t = int(input())


for num in range(1,t+1):
    r = [0,0,0,3,3,3,6,6,6]
    c = [0,3,6,0,3,6,0,3,6]
    arr = [list(map(int, input().split())) for _ in range(9)]
    result = 0
    for i in range(9):
        for j in range(9):
            if arr[i].count(j+1) > 1:
                result = 1
                break

    for k in range(9):
        cnt = 0
        for i in range(3):
            for j in range(3):
                cnt += arr[i + r[k]][j +c[k]]
        if cnt == 45:
            result = 1
            break


                                         
    
    if result == 1:
        print(f'#{num} 0')
    elif result == 0:
        print(f'#{num} 1')
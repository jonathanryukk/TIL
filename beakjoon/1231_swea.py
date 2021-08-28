import sys
sys.stdin = open('input.txt')

def in_order(v):
    if len(arr[v]) == 4:
        in_order(int(arr[v][2]))
        print(arr[v][1], end='')
        in_order(int(arr[v][3]))

    elif len(arr[v]) == 3:
        in_order(int(arr[v][2]))
        print(arr[v][1], end='')

    else:
        print(arr[v][1], end='')

    return


for tc in range(1, 11):
    n = int(input())
    arr = [[0]] + [list(map(str, input().split())) for _ in range(n)]
    print(f'#{tc}',end=' ')
    in_order(1)
    print()
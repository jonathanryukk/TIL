t = int(input())

def dfs(x,grade,cal):
    global result
    if cal > L:
        return
    if grade > result:
        result = grade
    if x == N:
        return
    dfs(x+1,grade,cal)
    dfs(x+1,grade+arr[x][0],cal+arr[x][1])


for tc in range(1, t + 1):
    N, L = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    result = 0
    dfs(0,0,0)

    print(f'#{tc} {result}')
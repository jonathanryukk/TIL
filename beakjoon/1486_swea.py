t = int(input())


def find(x, cur_result):
    global result
    if cur_result >= result:
        return
    if x >= N:
        if cur_result >= B:
            result = cur_result
        return

    visited[x] = 1
    find(x + 1, cur_result + arr[x])
    visited[x] = 0
    find(x + 1, cur_result)


for tc in range(1, t + 1):
    N, B = map(int, input().split())
    arr = list(map(int, input().split()))
    result = 99999999
    visited = [0] * N
    find(0, 0)
    print(f'#{tc} {result-B}')

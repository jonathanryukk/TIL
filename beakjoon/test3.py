import sys
sys.stdin = open("input.txt","r")
# 99행에 도착지점 2가 어떤 열에 있는지 찾는다
# 찾은 2 부터 좌 우 상 3가지 방향으로 움직인다

#0좌 1상 2우
dx = [0, -1, 0]
dy = [-1, 0, 1]
#사다리타기 규칙
# 위보다는 좌우에 길이 있으면 좌우 우선
# 내가 왔던 길을 돌아가지 않기
# 100*100 범위를 벗어나지않기
def find(col):
    curr = 99
    curc = col

    newr0 = curr+dx[0]
    newc0 = curc+dy[0]
    newr1 = curr+dx[1]
    newc1 = curc+dy[1]
    newr2 = curr+dx[2]
    newc2 = curc+dy[2]

    while arr[0][curc] != 1: # (1행, ?열) 1에 도착하면 멈춘다
        # 오른쪽에 길이 있으면 오른쪽으로
        if arr[newr2][newc2] == 1 and 0 <= arr[newr2][newc2] <= 99:
            #내가 왔던 길이면 가면안돼
            if arr[curr][curc] != arr[newr0][newc0]:
                curr = newr2
                curc = newc2
        # 왼쪽에 길이 있으면 왼쪽으로
        elif arr[newr0][newc0] == 1 and 0 <= arr[newr0][newc0] <= 99:
            #내가 왔던 길이면 가면안돼
            if arr[curr][curc] != arr[newr2][newc2]:
                curr = newr0
                curc = newc0
        # 위에 길이 있으면 위쪽으로
        elif arr[newr1][newc1] == 1 and 0 <= arr[newr1][newc1] <= 99:
            if arr[curr][curc] != arr[newr2][newc2] or arr[curr][curc] != arr[newr0][newc0]:
                curr = newr1
                curc = newc1

    return curc # 그때의 열을 반환하면 1행 curc열에 1이 있다.

T = 10
for tc in range(1,11):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]

    for i in range(100):
        if arr[99][i] == 2:
            result = find(i)

    print(f'#{tc} {result}')
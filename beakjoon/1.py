t = int(input())



for num in range(1,t+1):
    N = int(input())
    data = [list([0] * 10) for _ in range(10)]

    for inp in range(N):
        x1, y1, x2, y2, color = map(int, input().split())
        for i in range(x1,x2+1):
            for j in range(y1, y2+1):
                if data[i][j] == 0:
                    data[i][j] = color
                if data[i][j] == 1:
                    if color == 2:
                        data[i][j] += color
                    else:
                        pass
                if data[i][j] == 2:
                    if color == 1:
                        data[i][j] += color
                    else:
                        pass

    cnt = 0
    for i in range(10):
        for j in range(10):
            if data[i][j] == 3:
                cnt +=1
    print(f'#{num} {cnt}')
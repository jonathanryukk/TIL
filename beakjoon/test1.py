t = int(input())

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

for num in range(1+t+1):
    N = int(input())
    BRD = [[0]*N for _ in range(N)]
    
    value = 1
    R = 0
    C = 0
    while calue <= N**2:
        BRD[R][C] = value

        if  R < 0 or C < 0

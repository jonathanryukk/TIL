X, Y = map(int, input().split())
N = int(input())
max_x = 0
max_y = 0
for _ in range(N):
    X1, Y1 = map(int, input().split())
    if X1 == 0:
        if Y - Y1 > max_x:
            max_x = Y - Y1
    else:
        if X - Y1 < max_y:
            max_y = X - Y1
if max_x < X - max_x:
    max_x = X - max_x

if max_y < Y - max_y:
    max_y = Y - max_y
print(max_x, max_y)

print(max_x * max_y)

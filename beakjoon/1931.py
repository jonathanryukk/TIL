t = int(input())

time = []
for i in range(t):
    time.append(input().s)

min1 = 0
cnt = 0
for i in time:
    if i[3] < min1:
        min1 = i[3]
cnt += 1
for i in time():
    if i[3] < min1:
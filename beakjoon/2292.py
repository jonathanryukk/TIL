t = int(input())
cnt = 0
sum = 1
while cnt >= 0:
    sum += cnt * 6
    if t <= sum:
        print(cnt+1)
        break
    else:
        cnt += 1

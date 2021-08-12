A = int(input())
real_A = A
cnt =0
temp = 0
new = 0
while True:
    temp = A // 10 + A % 10 
    new = (A % 10)*10 + temp % 10
    A = new
    cnt = cnt +1
    if new == real_A:
        break
print(cnt)

    
t = int(input())
cnt = 0
num = 0
while True:
    if '666' in str(num):
        cnt += 1
    if cnt == t:
        print(num)
        break
    num += 1

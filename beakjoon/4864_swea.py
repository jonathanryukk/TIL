t = int(input())
for num in range(1,t+1):
    a = input()
    b = input()

    if a in b:
        print(f'#{num} 1')
    else:
        print(f'#{num} 0')
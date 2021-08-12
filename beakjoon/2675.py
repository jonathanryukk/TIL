t = input()
for num in range(int(t)):
    a,b = input().split()

    for i in range(len(b)):
        for j in range(int(a)):
            print(b[i],end='')
    print('')
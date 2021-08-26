N = int(input())

list6 = []

for i in range(N):
    list6.append(list(map(int, input().split())))

change = {0: 5, 1: 3, 2: 4, 3: 1, 4: 2, 5: 0}

for i in range(6):
    list1 = [i]
    list1.append(change[i])

    for j in range(6)
        list
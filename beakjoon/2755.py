lst = [[0 for j in range(14)] for i in range(15)]
for i in range(15):
    lst[i][0] = 1
for h in range(14):
    lst[0][h] = h+1
for i in range(1,15):
    for j in range(1,14):
        lst[i][j] = lst[i][j - 1] + lst[i - 1][j]

Test_case = int(input())
for i in range(Test_case):
    k = int(input())
    n = int(input())
    print(lst[k][n-1])
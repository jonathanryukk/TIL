t = int(input())

for i in range(t):
    a = input()
    sum = 0
    for j in a:
        if j =='O':
            sum = sum+1
            result = result+sum
        elif j == 'X':
            sum = 0
    print(result)

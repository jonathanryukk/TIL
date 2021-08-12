dial = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']

a = input()

result = 0

for i in range(len(a)):
    for j in dial:
        if a[i] in j:
            result = result + dial.index(j) + 3


print(result)

#apple 01234 
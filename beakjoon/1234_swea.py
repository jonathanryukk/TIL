import sys
sys.stdin = open('input1.txt')

for num in range(1,11):
    a,b = input().split()

    result = []

    for i in range(len(b)):
        if len(result) ==0:
            result.append(b[i])
        elif result[-1] != b[i]:
            result.append(b[i])
        else:
            result.pop(-1)
    result = ''.join(result)
    print(f'#{num} {result}')
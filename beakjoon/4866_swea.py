def push(result, n):
    result.append(n)

def pop(result):
    result.pop(-1)


t = int(input())

for num in range(1, t + 1):
    a = input()
    result = []
    ans = 1
    for i in a:
        if i == '(':
            push(result, i)
        if i == '{':
            push(result, i)
        if i == ')':
            if len(result) == 0:
                ans = 0
                break
            if result[-1] == '(':
                pop(result)
            else:
                ans = 0
                break
        if i == '}':
            if len(result) == 0:
                ans = 0
            if result[-1] == '{':
                pop(result)
            else:
                ans = 0
                break
    if len(result) > 0:
        ans = 0

    print(f'#{num} {ans}')

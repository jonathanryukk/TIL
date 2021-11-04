t = 10

for tc in range(1, t + 1):
    n = int(input())
    before = input()
    after = ''
    ST = []

    for i in before:
        if not ST and i == '+':
            ST.append(i)
        elif ST and i == '+':
            after += ST.pop()
            ST.append(i)
        else:
            after += i
    after += ST.pop()
    calculate= []

    for i in after:
        if i != '+':
            calculate.append(int(i))
        else:
            calculate.append(calculate.pop()+calculate.pop())
    print(f'#{tc} {calculate[0]}')
t = int(input())
for tc in range(1, t + 1):
    n = int(input())
    word = list(map(str, input().split()))
    cnt = 0
    lst = []

    print(word)
    for i in word:
        if i[-1] == '.' or i[-1] == '!' or i[-1] == '?':
            if i[0].isupper():
                if i[1:-1:].islower() and i[1:-1:].isalpha():
                    cnt += 1
                if len(i) == 2:
                    cnt += 1
            lst.append(cnt)
            cnt = 0

        else:
            if i[0].isupper():
                if i[1:].islower() and i[1::].isalpha():
                    cnt += 1
                if len(i) == 1:
                    cnt += 1
    print(f'#{tc}', end=" ")
    print(*lst)

keypad = [[], [], ['a', 'b', 'c'], ['d', 'e', 'f'], ['g', 'h', 'i'], ['j', 'k', 'l'], ['m', 'n', 'o'],
          ['p', 'q', 'r', 's'], ['t', 'u', 'v'], ['w', 'x', 'y', 'z']]

t = int(input())

for tc in range(1, t + 1):
    s, n = map(int, input().split())
    s = str(s)
    s = list(s)
    arr = list(input().split())


    result = 0
    for i in range(n):
        cnt = len(arr[i])
        cntcheck = 0
        for j in range(len(arr[i])):
            if arr[i][j] in keypad[int(s[j])]:
                cntcheck += 1
        if cntcheck == cnt:
            result += 1

    print(f'#{tc} {result}')

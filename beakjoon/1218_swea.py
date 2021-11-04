t = 10

for tc in range(1, t + 1):
    n = int(input())
    arr = list(input())
    cnt1, cnt2, cnt3, cnt4 = 0, 0, 0, 0
    result = 1
    for i in arr:
        if i == '(':
            cnt1 += 1
        elif i == '[':
            cnt2 += 1
        elif i == '{':
            cnt3 += 1
        elif i == '<':
            cnt4 += 1
        elif i == ')':
            cnt1 -= 1
            if cnt1 < 0:
                result = 0
                break
        elif i == ']':
            cnt2 -= 1
            if cnt2 < 0:
                result = 0
                break
        elif i == '}':
            cnt3 -= 1
            if cnt3 < 0:
                result = 0
                break
        elif i == '>':
            cnt4 -= 1
            if cnt4 < 0:
                result = 0
                break

    if result == 0 or cnt1 !=0 or cnt2 !=0 or cnt3 !=0 or cnt4 !=0:
        print(f'#{tc} 0')
    else:
        print(f'#{tc} 1')

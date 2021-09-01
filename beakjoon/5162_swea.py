t = int(input())
for tc in range(1, t + 1):
    A, B, C = map(int, input().split())

    result = 0

    if A > B:
        if C % B == 0:
            result = C / B

        else:
            result = C // B
            cnt = C % (B - 1)
            result += (cnt // A)

    else:
        if C % A == 0:
            result = C / A

        else:
            result = C // A
            cnt = C % (A - 1)
            result += (cnt // B)

    print(f'#{tc} {int(result)}')

T = int(input())
for tc in range(1, T+1):
    str1, str2 = input().split()
    result = str1.replace(str2,' ')

    print(f'#{tc} {len(result)}')

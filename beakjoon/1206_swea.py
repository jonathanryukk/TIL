for test1 in range(1,11):

    t = int(input())

    a = list(map(int,input().split()))
    #조망권이 있는 층의 갯수
    result = 0


# 입력받은 list인 a의 길이만큼 반복
    for i in range(2,len(a)-2):
        cnt = 0
#cnt 는 층수
        while cnt <= a[i]:
            if cnt > a[i-1] and cnt > a[i-2] and cnt > a[i+1] and cnt > a[i+2]:
                result += 1
            cnt += 1

    print(f'#{test1} {result}')

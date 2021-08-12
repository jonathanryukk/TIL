#테스트케이스 입력#
t = int(input())

for i in range(1,t+1):
    A = input()
    if A == A[::-1]:
        print(f'#{i} {1}')
    else:
        print(f'#{i} {0}')
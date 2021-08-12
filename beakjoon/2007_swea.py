t = int(input())

for i in range(1,t+1):
    A = str(input())
    A_list =list(A)
    for j in range(1,11):
        if A_list[0:j] == A_list[j:2*j]:
            print(f'#{i} {j}')
            break
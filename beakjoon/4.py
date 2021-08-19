import sys
sys.stdin = open("sample_input (3).txt","r")

def sel_sort(a):
    n = len(a)
    for i in range(0, n - 1):
        min_idx = i
        for j in range(i + 1, n):
            if a[j] < a[min_idx]:
                min_idx = j

        a[i], a[min_idx] = a[min_idx], a[i]
    return a

t = int(input())

for num in range(1,t+1):
    N = int(input())
    list1 = []
    arr = list(map(int, input().split()))

    arr = sel_sort(arr)

    for i in range(1,N+1):
        if i%2 == True:
            list1.append(arr[N-1-(i//2)])
        else:
            list1.append(arr[(i//2)-1])

    print(f'#{num} ',end='')
    for i in range(10):
        print(f'{list1[i]} ',end='')
    print('')
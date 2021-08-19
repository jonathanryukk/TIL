import sys
sys.stdin = open('input.txt')

def dfs(s):
    visit[s] = False
    for x in list1[s]:
        if visit[x] == True:
            dfs(x)


for w in range(10):
    num, V = map(int, input().split())

    arr = list(map(int, input().split()))
    list1 = [[] for _ in range(101)]
    visit = [True for _ in range(101)]
    
    list_arr = list(range(0,2*V,2))

    for i in list_arr:
        list1[arr[i]].append(arr[i+1])

    dfs(0)
    result = 1
    if visit[99] == True:
        result = 0

    print(f'#{num} {result}')

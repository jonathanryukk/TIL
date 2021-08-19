import sys

sys.stdin = open('sample_input.txt')


def dfs1(s):
    visit[s] = False
    for i in list1[s]:
        if visit[i] == True:
            dfs1(i)

t = int(input())

for num in range(1, t + 1):
    V, E = map(int, input().split())
    list1 = [[] for _ in range(V + 1)]
    visit = [True for _ in range(V + 1)]

    for i in range(E):
        a, b = map(int, input().split())
        list1[a].append(b)

    s, e = map(int, input().split())
    dfs1(s)
    result = 1
    if visit[e] == True:
        result = 0

    print(f'#{num} {result}')

import sys
from itertools import combinations

input = sys.stdin.readline

l, c = map(int, input().split())
lst = list(map(str, input().split()))
lst.sort()
comb = combinations(lst, l)
moum = ['a', 'e', 'i', 'o', 'u']
res = []

for c in comb:
    jcnt = 0
    mcnt = 0
    for i in range(l):
        if c[i] in moum:
            mcnt += 1
        else:
            jcnt += 1
        if mcnt >= 1 and jcnt >= 2:
            print(''.join(c))

import sys

N, M = map(int, sys.stdin.readline().strip().split())
set_d = set()
set_b = set()

for i in range(N):
    set_d.add(sys.stdin.readline().strip())
for i in range(M):
    set_b.add(sys.stdin.readline().strip())

result = list(set_d & set_b)
#
# for i in list_d:
#     for j in list_b:
#         if i == j:
#             result.append(i)
result.sort()
print(len(result))
for i in result:
    print(i)
list = []
for i in range(1,11):
    A = int(input())%42
    if A not in list:
        list.append(A)

print(len(list))
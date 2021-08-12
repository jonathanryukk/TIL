list1 = []

for i in range(9):
    list1.append(int(input()))

print(max(list1))
result = list1.index(max(list1))
print(result+1)
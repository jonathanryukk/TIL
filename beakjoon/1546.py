t = int(input())

list = list(map(int, input().split()))

max1 = max(list)

new_list = []

for i in range(t):
    new_list.append((list[i]/max1)*100)

AVG = sum(new_list)/ len(new_list)
print(AVG)
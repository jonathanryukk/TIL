t = int(input())

list_i = list(map(int, input().split()))

list_i2 = sorted(list_i)

result = 0

for i in range(t,0,-1):
    result += i * list_i2[t-i] 

print(result)
arr = input().split('-')

sumV = 0

for i in range(len(arr)):
    if '+' in arr[i]:
        new_a = arr[i].split('+')
        new_a = list(map(int, new_a))
        sumV += sum(new_a)
        arr[i] = '0'
result_arr = list(map(int, arr))

real_result = 0
for i in range(1,len(result_arr)):
    real_result += result_arr[i]

print(sumV)
print(real_result)
print(result_arr)
result = result_arr[0] - sumV - real_result

print(result)



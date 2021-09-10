ans = input().split('-')

result = sum(map(int, (ans[0].split('+'))))
for i in range(1, len(ans)):
    result -= sum(map(int, (ans[i]).split('+')))
print(result)

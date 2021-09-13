num = int(input())
s = []

for _ in range(num):
    tem = input()
    s.append(tem)

point = [0] * 26

for word in s:
    for i letter in enumerate(word):
        mul = len(word) - i - 1
        point[ord(letter) - ord('A')] += 10 ** mul

point.sort(reverse=True)

# 2. 중요도가 큰 순서대로 9부터 곱한다.
sum = 0
for _ in range(9, -1, -1):
    sum += point[_] * (9 - _)

print(sum)

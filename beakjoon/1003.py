case = [0] * 101
case[0], case[1], case[2] = 1, 1, 1
for i in range(3,101):
    case[i] = case[i-2] + case[i-3]

t = int(input())
for tc in range(t):
    print(case[int(input())-1])

E, S, M = map(int, input().split())

ans_E, ans_S, ans_M, cnt = 1, 1, 1, 1

while True:
    if ans_E == E and ans_S == S and ans_M == M:
        break
    ans_S += 1
    ans_M += 1
    ans_E += 1

    if ans_E >= 16:
        ans_E -= 15
    if ans_S >= 29:
        ans_S -= 28
    if ans_M >= 20:
        ans_M -= 19

    cnt += 1

print(cnt)

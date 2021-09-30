def inorder(node):
    global cnt
    if node == 0:
        return
    cnt += 1
    inorder(left[node])
    inorder(right[node])


for test_case in range(1, int(input()) + 1):
    E, N = map(int, input().split())
    arr = list(map(int, input().split()))
    left = [0] * (E + 2)
    right = [0] * (E + 2)
    for i in range(0, len(arr), 2):
        papa, baby = arr[i], arr[i + 1]
        if left[papa]:
            right[papa] = baby
        else:
            left[papa] = baby

    cnt = 0
    inorder(N)
    print('#{} {}'.format(test_case, cnt))
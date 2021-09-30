def postorder(root):
    s = tree[root]
    if s[0].isdecimal():
        return int(s[0])
    else:
        left = postorder(int(s[1]))
        right = postorder(int(s[2]))
        if s[0] == '+':
            return left + right
        elif s[0] == '-':
            return left - right
        elif s[0] == '*':
            return left * right
        elif s[0] == '/':
            return left / right


TC = 10
for tc in range(1, TC + 1):
    N = int(input())
    tree = [[] for _ in range(N + 1)]
    for i in range(N):
        s = list(input().split())
        node = int(s[0])
        tree[node] = s[1:len(s)]
    print('#{} {}'.format(tc, int(postorder(1))))
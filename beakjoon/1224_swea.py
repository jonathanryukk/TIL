calc = ['+',  '*', '(', ')']
inorder = {'+': 1, '*':2, '(': 0}
outorder = {'+': 1, '*':2, '(': 3}

def change(words):
    s = []
    top = -1
    result = ''
    for i in range(len(words)):
        if words[i] in calc:
            if s:
                if words[i] == ')':
                    while s[top] != '(':
                        result += s.pop()
                        top -= 1
                    s.pop()
                    top -= 1
                else:
                    while s and outorder[words[i]] <= inorder[s[top]]:
                        now = s.pop()
                        result += now
                        top -= 1
                    s.append(words[i])
                    top += 1
            else:
                s.append(words[i])
                top += 1
        else:
            result += words[i]
    while s:
        result += s.pop()

    return result

def calculation(words):
    s = []
    top = -1
    for i in range(len(words)):
        if words[i] in calc:
            if words[i] == '+':
                a, b = int(s.pop()), int(s.pop())
                s.append(b+a)
                top -= 1
            elif words[i] == '*':
                a, b = int(s.pop()), int(s.pop())
                s.append(b * a)
                top -= 1
        else:
            s.append(words[i])
            top += 1
    return s[0]
T = 10
for num in range(1,T+1):
    n = int(input())
    words = input()
    changes = change(words)
    print(f'#{num} {calculation(changes)}')
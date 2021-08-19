t = int(input())


def booknum(P,Pa):
    cnt = 0
    l = 1
    r = P
    c = int((l + r) / 2)
    while c != Pa:
        if c > Pa:
            r = c
            c = int((l + r) / 2)
            cnt +=1
        else:
            l = c
            c = int((l + r) / 2)
            cnt +=1
    return cnt

for num in range(1,t+1):
    A,B,C = map(int, input().split())
    cntA = booknum(A,B)
    cntB = booknum(A,C)
    if cntA > cntB:
        print(f"#{num} B")
    elif cntA == cntB:
        print(f"#{num} 0")
    else:
        print(f"#{num} A")
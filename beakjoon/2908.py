A,B = map(list,input().split())

ch_A = A[::-1]
ch_B = B[::-1]

real_A = "".join(map(str,ch_A))
real_B = "".join(map(str,ch_B))


if int(real_A) > int(real_B):
    print(real_A)
else:
    print(real_B)
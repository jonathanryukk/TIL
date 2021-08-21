A = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

T = input()
cnt = 0
for i in range(len(T)-1):
    if T[i]+T[i+1] in A:
        cnt -= 1
for i in range(len(T)-2):
    if T[i]+T[i+1]+T[i+2] in A:
        cnt -=1
print(cnt+len(T))
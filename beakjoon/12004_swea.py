googoodan=[]
for i in range(1,10):
    for j in range(1,10):
        googoodan.append(i*j)
googoodan= list(set(googoodan))

t= int(input())
for tc in range(1,t+1):
    N = int(input())

    if N in googoodan:
        print(f'#{tc} Yes')
    else:
        print(f'#{tc} No')




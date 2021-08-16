t = int(input())

for num in range(1,t+1):
    result = [0,0,0,0,0,0,0,0,0,0]
    en_list = ['ZRO', 'ONE', 'TWO', 'THR', 'FOR', 'FIV', 'SIX', 'SVN', 'EGT', 'NIN']
    c = input()
    arr = input().split()

    for i in arr:
        if 'ZRO' in i:
            result[0] += 1
        elif 'ONE' in i:
            result[1] += 1
        elif 'TWO' in i:
            result[2] += 1
        elif 'THR' in i:
            result[3] += 1
        elif 'FOR' in i:
            result[4] += 1
        elif 'FIV' in i:
            result[5] += 1
        elif 'SIX' in i:
            result[6] += 1
        elif 'SVN' in i:
            result[7] += 1
        elif 'EGT' in i:
            result[8] += 1
        elif 'NIN' in i:
            result[9] += 1

    result_list =[]

    for i in range(len(result)):
        for j in range(result[i]):
            result_list.append(en_list[i])

    result_list = ' '.join(result_list)

    print(f'#{num}\n{result_list}')
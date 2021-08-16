import sys
sys.stdin = open('GNS_test_input.txt')

t = int(input())

for num in range(1,t+1):
    result = []
    c = input()
    arr = input().split()

    for i in arr:
        if 'ZRO' in i:
            result.append('0')
        elif 'ONE' in i:
            result.append('1')
        elif 'TWO' in i:
            result.append('2')
        elif 'THR' in i:
            result.append('3')
        elif 'FOR' in i:
            result.append('4')
        elif 'FIV' in i:
            result.append('5')
        elif 'SIX' in i:
            result.append('6')
        elif 'SVN' in i:
            result.append('7')
        elif 'EGT' in i:
            result.append('8')
        elif 'NIN' in i:
            result.append('9')

    srt_r = sorted(result)
    list1 = []

    for i in srt_r:
        if '1' in i:
            list1.append('ONE')
        elif '2' in i:
            list1.append('TWO')
        elif '3' in i:
            list1.append('THR')
        elif '4' in i:
            list1.append('FOR')
        elif '5' in i:
            list1.append('FIV')
        elif '6' in i:
            list1.append('SIX')
        elif '7' in i:
            list1.append('SVN')
        elif '8' in i:
            list1.append('EGT')
        elif '9' in i:
            list1.append('NIN')
        elif '0' in i:
            list1.append('ZRO')

    result_list = ' '.join(list1)
    print(f'#{num}\n{result_list}')
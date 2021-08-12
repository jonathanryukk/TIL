#  ord(아스키) > 아스키코드 반환 chr(숫자) -> 숫자>아스키
a = input()

list_a = list(a)

for i in range(97,123):
    if chr(i) in list_a:
        print(list_a.index(chr(i)),end=' ')
    else:
        print(-1,end=' ')

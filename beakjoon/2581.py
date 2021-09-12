min_num = int(input())
max_num = int(input())
decimal_list = []

for i in range(min_num, max_num + 1):  # 첫 입력값과 두번째 입력값 사이만 진행
    count = 0
    for j in range(1, i + 1):  # 1부터 i항까지 진행
        if i % j == 0:
            count += 1  # 나뉘면 count증가
            if count > 2:  # 2보다 크면 소수가 아니므로(소수는 1과 자기자신으로만 나뉨) 바로 다음식 진행
                break
    if count == 2:  # 소수
        decimal_list.append(i)
if len(decimal_list) != 0:  # 소수리스트에 값이 있다면 밑의 값을 출력
    print(sum(decimal_list))
    print(decimal_list[0])
else:  # 소수가 하나도 없다면
    print('-1')
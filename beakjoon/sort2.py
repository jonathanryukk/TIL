import random # random 메소드 사용을 위해 import

a = random.sample(range(1, 10), 5) # 1<= x < 10의 난수 5개 리스트로 생성
print(a)# 정렬 전 리스트
print('')
for i in range(len(a)-1): # 리스트의 크기-1만큼 반복
    for j in range(i+1, len(a)): # 해당 인덱스+1부터, 리스트 크기만큼 반복
        if a[i] > a[j]: # 인덱스의 값이 비교 인덱스보다 더 크다면
            a[i] , a[j]  = a[j], a[i] # swap 해주기
print('')
print(a) # 정렬 후 리스트

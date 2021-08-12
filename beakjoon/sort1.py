import random # random 메소드 사용을 위해 import

a = random.sample(range(1, 10), 5) # 1<= x < 10의 난수 5개 리스트로 생성
print(a) # 정렬 전 리스트
print('')
for i in range(1, len(a)): # 리스트의 크기만큼 반복
    for j in range(0, len(a)-1): # 각 회전당 정렬이 끝나지 않은 친구들을 위해 반복
        if a[j] > a[j+1]: # 현재 인덱스의 값이 다음 인덱스의 값보다 크면 실행
           a[j+1], a[j] = a[j], a[j+1] # swap해서 위치 바꾸기
print('')
print(a) # 정렬 후 리스트
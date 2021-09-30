T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N, M, L = map(int, input().split())  # 노드의 개수, 리프 노드의 개수, 출력할 노드 번호
    lst = [0] * (N + 1)  # 노드의 개수+1만큼 트리 생성
    for _ in range(M):  # 트리에 리프 노드 데이터 삽입
        idx, data = map(int, input().split())  # 리프 노드 번호, 수
        lst[idx] = data
    for i in range(N - M, 0, -1):
        try:
            lst[i] = lst[i * 2] + lst[i * 2 + 1]  # 리프 노드를 제외한 노드=자식 노드에 저장된 값의 합
        except:
            lst[i] = lst[i * 2]  # 오른쪽 자식이 없을 경우

    print(f"#{test_case} {lst[L]}")
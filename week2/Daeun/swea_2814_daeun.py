T = int(input())  # 테스트 케이스의 수 입력
for test_case in range(1, T+1):
    n, m = map(int, input().split())  # n: 노드 수, m: 간선 수
    arr = [[] for _ in range(n+1)]  # 그래프를 저장할 리스트 (노드 번호 1번부터 시작하므로 n+1)
    visited = [0] * (n+1)  # 방문 여부를 기록하는 리스트
    max_cnt = 0  # 최대로 방문한 노드 수를 기록할 변수

    # 간선 정보를 입력받아 그래프 생성
    for _ in range(m):
        a, b = map(int, input().split())
        arr[a].append(b)  # 노드 a와 b를 서로 연결
        arr[b].append(a)

    # DFS 함수 정의
    def dfs(target, cnt):
        global max_cnt  # 전역변수 max_cnt를 사용
        visited[target] = 1  # 현재 노드 방문 처리

        if cnt > max_cnt:  # 현재까지의 방문 노드 수가 최댓값보다 크면 갱신
            max_cnt = cnt

        # 현재 노드와 연결된 다른 노드들에 대해 탐색
        for i in arr[target]:
            if visited[i] == 0:  # 방문하지 않은 노드만 탐색
                dfs(i, cnt + 1)  # 방문한 노드 수를 1 증가시키면서 재귀 호출

        visited[target] = 0  # 다른 경로 탐색을 위해 방문 처리 초기화

    # 각 노드를 시작점으로 DFS 수행
    for i in range(1, n+1):
        dfs(i, 1)  # 각 노드를 시작점으로 DFS 호출, 방문 노드 수는 1부터 시작

    # 결과 출력
    print("#{} {}".format(test_case, max_cnt))


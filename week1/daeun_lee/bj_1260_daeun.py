# 대부분 deque를 불러와서 사용한다. => bfs
# 그러나 굳이 불러오고 싶지 않다면 q.pop(0) 으로 제거해줘도 된다. -> 다만 오래걸리고 비효율적임.

from collections import deque  # deque를 사용하여 큐를 좀 더 효율적으로 사용

# 정점의 개수 n, 간선의 개수 m, 시작할 정점 v 입력 받기
n, m, v = map(int, input().split())

# 인접 행렬을 생성하여 간선 정보 저장 (정점 번호는 1부터 시작하므로 n+1 크기로 만든다.)
arr = [[0] * (n + 1) for _ in range(n + 1)]

# m개의 간선 입력 받아 인접 행렬에 입력해주기
for i in range(m):
    a, b = map(int, input().split())
    arr[a][b] = arr[b][a] = 1  # 무방향 그래프이므로 양쪽 방향 둘다 기록해준다. (문제에 간선은 양방향이라고 제시함)

# DFS와 BFS에서 방문 여부를 기록할 used 배열 정의
used_dfs = [0] * (n + 1)
used_bfs = [0] * (n + 1)

# 깊이 우선 탐색 (DFS) 함수 정의
def dfs(v):
    used_dfs[v] = 1  # 들어오자마자 방문했다는 표시
    print(v, end=' ')  # 방문한 정점 출력
    for i in range(1, n + 1):  # 1번 정점부터 n번 정점까지 반복
        if arr[v][i] == 0 or used_dfs[i] == 1:  # 연결된 곳이 없거나 이미 방문한 정점은 건너뛰기
            continue
        dfs(i)  # 위의 if 문 조건을 만족하지 않는다면 dfs 함수로 다시 들어가서 탐색

# 너비 우선 탐색 (BFS) 함수 정의
def bfs(v):
    q = deque([v])  # 들어오자마자 큐에 넣기
    used_bfs[v] = 1  # 방문한 곳 표시하기

    while q:  # 큐가 존재하는 동안 실행 > 즉 큐가 다 사라지면 while문 종료하자.
        v = q.popleft()  # 큐에서 가장 앞에 있는 정점을 꺼냄 - popleft
        print(v, end=' ')  # 방문한 정점 바로 출력
        for i in range(1, n + 1):  # 1번 정점부터 n번 정점까지 이 과정을 반복
            if arr[v][i] == 0 or used_bfs[i] == 1:  # dfs 함수와 마찬가지로 연결된 곳이 없거나 이미 방문한 정점은 건너뛴다.
                continue
            used_bfs[i] = 1  # 위의 if문 조건에 해당하지 않는다면, 방문해야한다. 방문 처리하고 q에 들어간다.
            q.append(i)  # 큐에 해당 정점도 추가해준다.

dfs(v)
print()  # 출력 형식 맞추기 위해 줄바꿈
bfs(v)

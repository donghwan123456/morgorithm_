# 운전해야하는 거리를 비용이라고 지칭하고 작성함.

import heapq  # 우선순위 큐 사용을 위해 heapq 모듈을 import

n, d = map(int, input().split())  # n: 지름길 개수, d: 고속도로의 길이
arr = [[] for _ in range(d + 1)]  # 그래프 초기화 (0부터 d까지)

result = int(21e8)  # 무한대를 큰 값으로 설정
distance = [result] * (d + 1)  # 거리 테이블을 모두 무한대로 초기화

# 고속도로의 모든 지점에서 다음 지점으로 가는 기본 비용을 1로 설정
# 설정해야하는 이유 => 지름길이 없는 경우에 대비하기 위해서
# 기본 비용 설정하지 않으면 지름길이 없는 구간 처리가 누락될 수 있다.
for i in range(d):
    arr[i].append((i + 1, 1))

# 지름길 정보 입력
for _ in range(n):
    start, end, short_line = map(int, input().split())
    if end > d:  # 지름길의 끝이 고속도로의 범위를 벗어나면 무시
        continue
    arr[start].append((end, short_line))  # 지름길 정보를 그래프에 추가

# 다익스트라 알고리즘을 위한 초기 설정
heap = []
heapq.heappush(heap, (0, 0))  # 시작 지점(0)에서의 거리는 0으로 설정
distance[0] = 0  # 시작 지점에서의 거리는 0

# 다익스트라 알고리즘 실행
while heap:
    dist, now = heapq.heappop(heap)  # 가장 짧은 거리를 가진 노드를 선택
    if dist > distance[now]:  # 이미 처리된 노드면 무시
        continue
    for next_node, cost in arr[now]:
        new_cost = dist + cost  # 현재 노드를 거쳐서 가는 비용 계산
        if new_cost < distance[next_node]:  # 더 짧은 경로가 발견되면 업데이트
            distance[next_node] = new_cost
            heapq.heappush(heap, (new_cost, next_node))  # 갱신된 경로를 우선순위 큐에 삽입

# 최종 목적지(d)까지의 최단 거리 출력
print(distance[d])

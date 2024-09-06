# 모음이 최소 하나, 자음 최소 두 개
# 오름 차순 정렬
# C개 알파벳으로 만든 조합 중 위 조건 만족하는 조합 갯수가 정답
from itertools import combinations
# 조합 만드는 함수 import
# sorted, combinations, join 사용

# 알고리즘 분류는 백트래킹인데 백트래킹보다 for문 먼저 떠오름
# 주어진 알파벳 오름차순 정렬 후 가능한 모든 조합 생성
# 가능한 조합 중 위의 조건(자음,모음 갯수) 만족하는 경우만 출력

L, C = map(int,input().split())
alpha_list_ = sorted(input().split())

# print(L, C, alpha_list_)
moeum = ['a', 'e', 'i', 'o', 'u']

# 가능한 전체 조합을 pos_list_에 만들어 놓기
pos_list_ = combinations(alpha_list_,L)

answer = []

# 전체 조합을 하나 씩 탐색
for i in pos_list_:
    moeum_count_ = 0
    jaeum_count_ = 0
    # 조합 안의 알파벳을 탐색
    # 알파벳이 모음 리스트 안에 있을 때, 없을 때 각각 cnt 추가
    for j in i:
        if j in moeum:
            moeum_count_ += 1
        else:
            jaeum_count_ += 1
    # 모음1개이상, 자음 2개이상으로 조건 충족하면 출력
    if moeum_count_>=1 and jaeum_count_>=2:
        # i 바로 출력하면 출력 형태 맞지 않음, ->('a', 'c', 'i', 's') 이렇게 출력됨
        answer = ("".join(i))
        print(answer)
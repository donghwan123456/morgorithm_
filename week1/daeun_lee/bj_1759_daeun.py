# 서로 다른 n개의 알파벳 개수, 후보 문자 갯수 m 입력 받기
n,m=map(int,input().split())

# 서로 다른 n개의 알파벳 리스트
alpha=list(map(str,input().split()))

# 알파벳 오름차순 정렬
alpha.sort()

# 알파벳을 담을 비밀번호 리스트
path=['']*n

# 모음, 자음 최소 갯수 제한이 있으므로
# 모음을 담은 리스트 활용
mo_um=['a','e','i','o','u']

# count_alpa:모음, 자음 개수를 판별하는 함수
def count_alpa(path):
    # mo : 모음, ja:자음
    mo = 0
    ja = 0
    # path 배열 (비밀번호 배열)의 요소들이 모음 리스트 안에 있다면 모음 +=1
    # 없다면 > 자음이다! 자음 +=1
    for i in path:
        if i in mo_um:
            mo+=1
        else:
            ja+=1
    return mo,ja

# 알파벳을 담는 dfs 함수
def dfs(st,level):
    # 기저조건: n개의 비밀번호를 다 뽑았다 > 리턴
    if level == n:
        # 우선 뽑힌 비밀번호가 모음, 자음 최소갯수를 만족해야 출력할 것이다.
        # 모음은 최소 1개, 자음은 최소 2개
        # count_alpa 함수에 보내서 확인해보자
        mo,ja=count_alpa(path)
        # count_alpa 함수 다녀왔는데 최소 갯수 만족하는 경우 프린트
        if mo >=1 and ja >=2:
            # 비밀번호 갯수가 level이 될 것이기 때문에 range가 level
            for i in range(level):
                print(path[i],end='')
            print()
        return

    # path 배열에 비밀번호 하나씩 담아주기 => 인덱스는 레벨
    # 그래야 다 담으면 끝냈을때 비밀번호가 완성된다.
    # 조합 => start에서 부터 쭉 본다.
    # 그렇다면? 다음 dfs에 들어갈때는 그 다음것부터 봐주면 된다.
    for i in range(st,m):
        path[level]=alpha[i]
        dfs(i+1,level+1)

# level은 0,start도 0 에서 시작
dfs(0,0)
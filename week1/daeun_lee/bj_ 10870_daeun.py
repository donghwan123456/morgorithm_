# 찾을 n번째 피보나치 수 입력
n=int(input())

# find_num:n번째 피보나치 수를 찾는 함수
def find_num(n):
    # n이 0, 1인 경우 n과 n번째 피보나치 수는 같다.
    if n<=1:
        return n

    # 그 외의 경우
    else:
        # 피보나치 수는 n-1번째 피보나치 수와 n-2번째 피보나치 수의 합이다.
        # 즉 바로 앞 수 2개를 더하면된다.
        # find_num 함수에 n-1일때와 n-2일때를 넣었다면 값을 얻을 수 있다.
        result=find_num(n-1)+ find_num(n-2)
        return result

# find_num 함수를 호출하여 리턴 받은 결과를 출력
print(find_num(n))
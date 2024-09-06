def sum_(n):
    if n <= 1:
        return n
    return sum_(n - 1) + sum_(n - 2)
n = int(input())
print(sum_(n))

#재귀 / for문으로도 가능하지만 재귀 학습 위해 재귀 형태로
#ex) n == 4이면
#sum_(4) -> sum_(3) + sum_(2) -> (sum_(2) + sum_(1)) + (sum_(1) + sum_(0))
# => sum_ = sum_(1) + sum_(1)
#이렇게
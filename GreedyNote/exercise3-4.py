# 실전 문제
# 4 1이 될 때까지

N, K = map(int, input().split(' '))
count = 0

while True:
    if N == 1:
        break
    elif N % K == 0:
        N //= K
        count += 1
    else:
        N -= 1
        count += 1


print(count)


# 문제가 약간 이상한거 같은데

# 실전 문제
# 2 큰 수의 법칙

# 배열의 크기 N 2 ~ 1,000
# 숫자가 더해지는 횟수 M
# 최대로 더할 수 있는 횟수 K
N, M, K = map(int, input().split(' '))
# N개의 자연수 1 ~ 10,000

str1 = list(map(int, input().split(' ')))
str1.sort()
# 가장 큰 수와 바로 그 다음 수만 알면된다.
a = str1.pop()
b = str1.pop()

result = 0
if a != b:
    # 이거 식 잘못됨 다시 해야함
    result = (M // (K + 1)) * ((a * K) + b)+((M -(M//(K+1))*(K+1))*a)
    
    
    print(result)
# 가장 큰 수와 바로 그 다음 수가 같으면 K번씩 계속 더한다.
else:
    result = a * M
    print(result)

# ex 4-1 상하좌우
# 알고리즘 문제를 푸는 환경에서는 GPU연산을 사용하지 않기 때문에
# C로 작성된 SW가 동작하는 것이 아니라 Python만 작동하기 때문에 실행 시간이 느리다

# 완전 탐색 : 모든 경우의 수를 다 계산하여 해결
# 시뮬레이션 : 문제에서 제시한 알고리즘을 한 단계씩 차례대로 직접 수행

# l, r, u, d

# 공간의 크기
N = int(input())
# 이동 횟수 =< 100
cur = [1, 1]
plan = map(str, input().split(' '))


def calMinus(std):
    if std == 1:
        return 0
    else:
        return 1


def calPlus(std):
    if std == N:
        return 0
    else:
        return 1


for block in plan:
    if block == 'R':
        cur[1] += calPlus(cur[1])
    elif block == 'L':
        cur[1] -= calMinus(cur[1])
    elif block == 'U':
        cur[0] -= calMinus(cur[0])
    elif block == 'D':
        cur[0] += calPlus(cur[0])
    else:
        pass
    
print(cur)

# 실전 문제
# 3 숫자 카드 게임
N, M = map(int, input().split(' '))
cards = list()
for _ in range(N):
    cards.append(list(map(int, input().split(' '))))

result = list()
for lst in cards:
    result.append(min(lst))


print(max(result))

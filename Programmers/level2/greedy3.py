# 구명 보트
input1 = [20, 70, 50, 80, 50]
input2 = 100
# 최대한 적게 보트를 사용하여 사람들을 구출해라


def solution_internet(people, limit):
    # 몸무게가 가장 큰 사람과 작은 사람을 비교해갔구나.
    people.sort()
    count = 0
    i = 0
    j = len(people)-1
    while i <= j:
        count += 1
        if people[j]+people[i]<=limit:
            i += 1
        j -= 1
    return count




# print(solution(input1, input2))

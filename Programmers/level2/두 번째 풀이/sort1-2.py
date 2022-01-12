# sorting lv2 두 번째 풀이
# 가장 큰 수
input1 = [6, 10, 2]
input2 = [3, 30, 34, 5, 9, 50, 52, 59]


def solution(numbers):
    numbers.sort(key=lambda x : str(x)*3, reverse=True)
    answer = str(int(''.join(map(str, numbers))))
    return answer


print(solution(input2))

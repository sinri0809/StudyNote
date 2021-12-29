input1 = [6, 10, 2]
input2 = [3, 30, 34, 5, 9]


def solution(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(key=lambda x: x * 3, reverse=True)
    print(numbers)
    return str(int(''.join(numbers)))

# lambda x*3의 이유는 num값이 1000이하이기 때문에 3자리수로 맞춘 뒤에 비교를 한다는 뜻이다.
# 문자열은 ascii값으로 치환되어 비교/정렬된다.

# 마지막으로 0000이 계속되는것을 방지하기 위해서 int로 바꿨다가 다시 str로 바꾼다.


print(solution(input1))
print(solution(input2))

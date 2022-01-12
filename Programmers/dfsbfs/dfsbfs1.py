# dfsbfs lv2 타겟 넘버
"""
음이 아닌 정수를 빼거나 더하여서 타겟 넘버(자연수)를 만든다.
타겟넘버를 만들 수 있는 경우의 수를 return
"""
input1 = [1, 2, 3, 4, 5]
# input1 = [1, 1, 1, 1, 1]
input2 = 3
# -1 1 1 1 1
# -1 -1 -1 1 1
# -1 -1 -1 -1 -1 0보다 작아지면 안됨.


def solution(numbers, target):
    # -1 곱하기 // -1을 곱할 숫자를 push하는 stack
    # 값이 음수거나 target이 아니면 pop
    stack = []
    
    # while len(stack) < len(numbers):
    for index in range(len(numbers)):
        applied = [1] * len(numbers)
    
        stack.append(index)
        applied[stack.pop()] = -1

        sum = 0
        print(applied)
        for i, j in zip(applied, numbers):
            sum += i * j
        print(sum)
        # if sum != target:
        #     stack.pop()


def bfs(numbers, target):
    leaves = [0]
    for num in numbers:
        tmp = []
        for parent in leaves:
            tmp.append(parent + num)
            tmp.append(parent - num)
        leaves = tmp.copy()
    # print(leaves)
    count = 0
    for t in leaves:
        if t == target:
            count += 1
    return count

print(bfs(input1, input2))


def dfs(numbers, target, depth):
    answer = 0
    if depth == len(numbers):
        print(numbers)
        if sum(numbers) == target:
            return 1
        else: return 0
    else:
        answer += dfs(numbers, target, depth+1)
        numbers[depth] *= -1
        answer += dfs(numbers, target, depth+1)
        return answer
    


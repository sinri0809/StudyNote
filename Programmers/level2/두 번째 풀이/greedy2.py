# greedy lv2 큰 수 만들기 두 번째 시도
def solution(number, k):
    stack = []
    
    for num in number:
        while k > 0 and stack and stack[-1]<num:
            stack.pop()
            k -= 1
        stack.append(num)
        
    print(stack)
    

print(solution("1924", 3))

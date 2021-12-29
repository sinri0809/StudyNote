# 💓💓solution
# 큰 수 만들기
input1 = '1231234'
input2 = 3


def solution(number, k):
    result = []
    
    for numb in number:
        result.append(numb)
        
        
    return result



def solution_sol(number, k):
    answer = []  # Stack
    
    for num in number:
        while k > 0 and answer and answer[-1] < num:
            answer.pop()
            k -= 1
        answer.append(num)
    
    return ''.join(answer[:len(answer) - k])


print(solution(input1, input2))

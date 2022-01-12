from itertools import permutations as permu
input1 = "0110011"

def chek_prime(number: int):
    # 소수 판별 원리 : n의 제곱근 보다 작은 숫자까지 나눠보고 나눠떨어지면 소수 아님
    if number < 2:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True


def solution(numbers):
    number_set = set()
    prime_stack = set()
    for i in range(1, len(numbers)+1):
        for j in permu(numbers, i):
            number_set.add(int(''.join(j)))
    
    for numb in number_set:
        if chek_prime(numb):
            print(numb)
            prime_stack.add(numb)
            
    print(prime_stack)
    return len(prime_stack)


print(solution(input1))

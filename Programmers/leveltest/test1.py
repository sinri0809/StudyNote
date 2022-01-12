n, m = 1,5


def solution(n, m):
    min_num = min(n, m)
    max_num = max(n, m)
    result_min = 1
    for i in range(2, min(n, m)):
        while min_num % i == 0 and max_num % i == 0:
            min_num = min_num // i
            max_num = max_num // i
            result_min *= i
    if result_min == 1:
        return [1, n*m]
    else:
        return [result_min, n*m//result_min]
    
print(solution(n, m))

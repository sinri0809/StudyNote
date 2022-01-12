input1 = 5
input2 = [2, 4] # lost
input3 = [1, 4] # reverse


def solution(n, lost, reserve):
    # 5번째 조건
    real_lost = set(lost)-set(reserve)
    real_reserve = set(reserve)-set(lost)
    result = n - len(real_lost)
    for loster in real_lost:
        for reserver in real_reserve:
            if loster-1 == reserver or loster+1 == reserver:
                real_reserve.remove(reserver)
                result += 1
                break
            
    
    
    return result


print(solution(input1, input2, input3))

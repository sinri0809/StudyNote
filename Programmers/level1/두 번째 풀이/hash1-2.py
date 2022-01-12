# hash lv1 2번째 풀이
# 완주하지 못한 선수
input1 = ["leo", "kiki", "eden"]
input2 = ["eden", "kiki"]


def solution(participant, completion):
    sum_part = 0
    part_dct = dict()
    for part in participant:
        part_dct[hash(part)] = part
        sum_part += hash(part)
        
    for comp in completion:
        sum_part -= hash(comp)
    
    answer = part_dct[sum_part]
    return answer


print(solution(input1, input2))

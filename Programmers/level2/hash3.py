# hash lv2
# 위장
"""
같은 이름을 가진 의상은 존재하지 않는다.
의상의 수는 1개 이상 30개 이하이다.
문자열의 길이는 1이상 20이하 자연수이며 알파벳 소문자와 _로 이루어져있다.
하루에 최소 한 개 의상은 입는다.
"""
# 서로 다른 옷의 조합의 수를 return
from functools import reduce
from collections import Counter as counter
from itertools import combinations as comb
# 꼭 전역적으로 import안해줘도 함수안에서 import하는 방법도 있음

input1 = [["yellowhat", "headgear"],
          ["bluesunglasses", "eyewear"],
          ["bluesunglasds", "eyewear"],
          ["bluesunglasds", "bottom"],
          ["bluesunglasds", "pin"],
          ["green_turban", "headgear"]]


def solution(clothes):
    # 두 번째 시도
    '''
    수학이 부족했음.
    :param clothes:
    :return:
    '''
    clothes_counter = counter(j for i, j in clothes)
    # 경우의 수 = 0개일 경우~a개일 경우: a+1 *(b+1)*(c+1)...  - 모두 0개인 경우 : 1
    answer = reduce(lambda x, y: (x)*(y+1), clothes_counter.values(), 1) - 1
    return answer
    

def solution_try1(clothes):
    # 시간 초과
    clothes_counter = counter()
    for cloth in clothes:
        clothes_counter += counter([cloth[1]])
        
    answer = 0
    for i in range(1, len(clothes_counter)+1):
        for tpl in comb(clothes_counter.values(), i):
            print(tpl)
            answer += reduce(lambda x,y:x*y, tpl)
    return answer

    # answer += sum(clothes_counter.values())
    # if len(clothes_counter) > 1:
    #     for i in range(2, len(clothes_counter)+1):
    #         for tpl in comb(clothes_counter.values(), i):
    #             answer += reduce(lambda x,y:x*y, tpl)

    return answer
    
    
print(solution(input1))

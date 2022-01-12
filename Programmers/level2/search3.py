# search lv2 카펫
"""
각 격자 수가 주어졌을 때
가로*세로 크기를 순서대로 배열에 담아 return하기
 세로가 더 작다.
"""
input1 = 24
input2 = 24

# 1*2 3*4-2
# 1*1 3*3
# 2*12 4*14
# 3*8 5*10
# 4*6 6*8


def solution(brown, yellow):
    total = brown + yellow
    for i in range(1, yellow+1):
        if yellow % i == 0 and (i+2)*((yellow//i)+2) == total:
            return sorted([((yellow//i)+2),(i+2)], reverse=True)
    
    

print(solution(input1, input2))

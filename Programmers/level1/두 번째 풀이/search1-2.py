# search lv1 두 번째 풀이
# 모의고사
input1 = [1,2,3,4,5]
# input1 = [1,3,2,4,2]
# input1 = [1,3,2,4,2,1,3,2,4,2,1,3,2,4,2]

# 가장 많은 문제를 맞춘사람이 누구인지.
def solution(answers):
    math_dct = {1: [1, 2, 3, 4, 5],
                2: [2, 1, 2, 3, 2, 4, 2, 5],
                3: [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]}
    math_correct = {1: 0, 2: 0, 3: 0}
    
    for i in math_dct:
        for j, k in zip(answers, math_dct[i]*(-(-len(answers)//len(math_dct[i])))): # 반올림해주려고 식이 복잡한것
            # 📌cycle이라는 librart를 쓸수도 있다.
            if j == k:
                math_correct[i] += 1
    
    max_score = max(math_correct.values())
    result = []
    for i in math_correct:
        if math_correct[i] == max_score:
            result.append(i)
        
    return result

print(solution(input1))

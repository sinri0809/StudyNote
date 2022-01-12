# greedy lv1 두 번째 풀이 체육복
"""
n 전체 학생 수 2~30
lost 도난당한 학생 번호, 중복은 없음
reserve 여분이 있는 학생 번호, 중복은 없음
도난 당한 학생이 여분이 있다면 본인 거 부터 챙김.
체육수업을 들을 수 있는 학생의 최댓값 return
"""
input1 = 5
input2 = [1, 3, 5]
input3 = [3, 4]


def solution(n, lost, reserve):
    lost = set(lost)
    reserve = set(reserve)
    real_lost = lost - reserve
    real_reserve = reserve - lost

    student = n - len(real_lost)
    
    for i in real_lost:
        if i+1 in real_reserve:
            real_reserve.remove(i+1)
            student += 1
        elif i-1 in real_reserve:
            real_reserve.remove(i-1)
            student += 1
    
    return student
    

print(solution(input1, input2, input3))

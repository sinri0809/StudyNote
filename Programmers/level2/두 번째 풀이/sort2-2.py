# sorting lv2 두 번째 풀이
# H-Index
"""
발표한 논문 n편 중
    h번 이상 인용된 논문이 h편 이상
    나머지 h번 이하
    h의 최댓값(H-Index) return
"""
input1 = [3, 0, 6, 1, 5]


def solution_enternet(citations):
    citations.sort(reverse=True)
    for idx , citation in enumerate(citations):
        if idx >= citation:
            return idx
    return len(citations) # 📌이게 이해가 안가네...


def solution(citations):
    citations.sort(reverse=True)
    for i, cit in enumerate(citations, 1):
        if i >= cit:
            return i
        


print(solution(input1))

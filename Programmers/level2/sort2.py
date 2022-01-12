input1 = [3, 0, 6, 5, 5, 4, 4]


def solution(citations):
    stack_set = set()
    result = 0
    for i in range(len(citations)):
        if citations[i] not in stack_set and result < citations[i]:
            stack_set.add(citations[i])
            upper = 0
            for j in range(len(citations)):
                if j == i:
                    pass
                elif j >= citations[i]:
                    upper += 1
    return result


print(solution(input1))

# 문제를 이해 못하고 있는거 같음...
def solution_2(citations):
    citations.sort(reverse=True)
    # enumerate(iteralbe, start=0) : index와 iterable의 값들을 tuple로 묶어준다.
    for idx , citation in enumerate(citations):
        if idx >= citation:
            return idx
    return len(citations)


def solution_again(citations):
    citations.sort(reverse=True)
    for i in range(len(citations)):
        if i >= citations[i]:
            return i
    return len(citations)

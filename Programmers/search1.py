# input1 = [1,3,2,4,2]
input1 = [1,2,3,4,5]



def solution(answers):
    person_1 = [1, 2, 3, 4, 5]
    person_2 = [2, 1, 2, 3, 2, 4, 2, 5]
    person_3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    result = list()
    count = [0] * 3
    for a in range(len(answers)):
        if person_1[a%5] == answers[a]:
            count[0] += 1
        if person_2[a%8] == answers[a]:
            count[1] += 1
        if person_3[a%10] == answers[a]:
            count[2] += 1
    result_arr = sorted(enumerate(count, start=1), key=lambda x: x[1], reverse=True)
    for val in result_arr:
        if val[1] == result_arr[0][1]:
            result.append(val[0])

    return result


print(solution(input1))

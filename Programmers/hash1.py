# solution
participant = ["mislav", "stanko", "mislav", "ana", "mislav"]
completion = ["stanko", "ana", "mislav", "mislav"]

def solution(participant, completion):
    partici_dict = dict()
    sum_hash = 0
    for part in participant:
        # hash(part) : 알수 없는 숫자가 들어가는데, key를 빠르게 비교할 수 있도록 해준다고 함.
        partici_dict[hash(part)] = part
        sum_hash += hash(part)
    
    for comp in completion:
        sum_hash -= hash(comp)
        
    return partici_dict[sum_hash]



import collections


def solution_liked(participant, completion):
    answer = collections.Counter(participant) - collections.Counter(completion)
    # counter : key가 이름이고 value가 counter인 dict자료형을 반환한다.
    return list(answer.keys())[0]


def solution2(participant, completion):
    participant.sort()
    completion.sort()
    for i in range(len(completion)):
        if (participant[i] != completion[i]):
            return participant[i]
    return participant.pop()
    
print(solution(participant, completion))

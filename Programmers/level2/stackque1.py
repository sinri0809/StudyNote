from collections import deque

input1 = [1, 30, 55]
input2 = [50, 30, 5]


def solution(progresses, speeds):
    progress_q = deque(progresses)
    speeds_q = deque(speeds)
    result = []
    while len(progress_q) > 0:
        count = 0
        for i in range(len(progress_q)):
            progress_q[i] += speeds_q[i]
        
        for i in range(len(progress_q)):
            if progress_q[0] >= 100:
                progress_q.popleft()
                speeds_q.popleft()
                count += 1
        if count > 0:
            result.append(count)
        
    return result


print(solution(input1, input2))


def solution_liked(progresses, speeds):
    Q=[]
    for p, s in zip(progresses, speeds):
        if len(Q)==0 or Q[-1][0]<-((p-100)//s):
            Q.append([-((p-100)//s),1])
        else:
            Q[-1][1]+=1
    return [q[1] for q in Q]


# zip 내장 함수
numbers = [1, 2, 3]
letters = ["a", "b", "c"]
for pair in zip(numbers, letters):
    print(pair)

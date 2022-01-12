# stackque lv2 프린터
# solution
"""
나머지 인쇄 대기목록에서 J보다 중요도가 높은 문서가 한 개라도 존재하면
J를 대기목록의 가장 //마지막//에 넣습니다.
 요청한 문서가 몇 번째로 인쇄되는지 return
"""
from collections import deque

# input1 = [2, 1, 3, 2]
input1 = [1, 1, 9, 8, 1, 9]
input2 = 2


def solution_enternet(priorities, location):
    arr1 = [c for c in range(len(priorities))]
    arr2 = priorities.copy()
    
    i = 0
    while True:
        if arr2[i] < max(arr2[i+1:]):
            arr1.append(arr1.pop())
            arr2.append(arr2.pop())
        else:
            i += 1
        
        if arr2 == sorted(arr2, reverse=True):
            break
    
    return arr1.index(location) + 1


def solution2(priorities, location):
    que = deque(priorities)
    
    i = 0
    while True:
        print(list(que)[i+1:])
        if max((list(que)[i+1:])) > que[i]:
            que.append(que.popleft())
            if location == 0:
                location = len(priorities) - 1
            else:
                location -= 1
        else:
            i += 1
            
        if list(que) == sorted(priorities, reverse=True):
            break
    
    print(location)


print(solution2(input1, input2))


def solution(priorities, location):
    prio_que = deque(priorities)
    
    for i in range(len(prio_que)):
        for j in list(prio_que)[1:]:
            if j > prio_que[0]:
                
                prio_que.append(prio_que.popleft())
                if location == 0:
                    location = len(priorities) - 1
                else:
                    location -= 1
    return location+1


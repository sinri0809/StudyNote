# stackque lv2 두 번째 풀이 프린터 🟢
# q = [(idx, priority) for (idx, priority) in enumerate(priorities)] 📌 이런식으로하면 que를 두 개만들지 않아도 됨

input1 = [2, 1, 3, 2, 9, 1]
input2 = 5


def solution(priorities, location):
    from collections import deque
    
    arr_q = deque(priorities)
    arr_location = deque([0] * len(priorities))
    arr_location[location] = 1

    while arr_q:
        cnt = 1
        for n in list(arr_q)[1:]:
            if arr_q[0] < n:
                cnt = 1
                arr_q.append(arr_q.popleft())
                arr_location.append(arr_location.popleft())
                break
            else:
                cnt += 1
        
        if cnt == len(arr_q):
            arr_q.popleft()
            if arr_location[0] == 1:
                return len(priorities) - len(arr_q)
            arr_location.popleft()


print(solution(input1, input2))

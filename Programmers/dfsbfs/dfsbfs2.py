# dfsbfs lv3 네트워크 🔺
"""
n 컴퓨터 개수 computers 연결정보
네트워크의 개수를 return
node 에서 node는 1이다.
"""
from collections import deque
input1 = 3
input2 = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]


def solution(n, computers):
    connected = 1 # connected의 갯수를 return
    stack =[]
    q = deque([0])

    while len(stack) < n:
        print(q)
        
        if len(q) == 0:
            connected += 1
            for n, st in enumerate(stack):
                if n != st:
                    now = n
        
        else:
            now = q.popleft()
            stack.append(now)
        
        for i, conn in enumerate(computers[now]):
            if conn == 1 and i != now:
                q.append(i)
    
    print(stack)


print(solution(input1, input2))

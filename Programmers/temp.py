from collections import deque

input1 = [93, 30, 55]
input2 = [1, 30, 5]



def solution(numbers, target):
    leaves = [0]
    for num in numbers:
        tmp = []
        for parent in leaves:
            tmp.append(parent + num)
            tmp.append(parent - num)
        leaves = tmp.copy()
    
    

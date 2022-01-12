# greedy lv3 조이스틱 🔺


def solution(name):
    answer = 0
    min_left_right = len(name)
    a = ord("A")
    z = ord("Z")
    next_idx = 0
    for idx, char in enumerate(name):
        answer += min(ord(char)-a, z-ord(char)+1)
        
        next_idx = idx + 1 # 바로 옆으로 갈때,
        while next_idx < len(name) and name[next_idx] == "A": # A가 있는 부분으로 갈 때,
            next_idx += 1
        
        # 한 방향으로만 이동하는 경우와 오른쪽으로 이동했다가 왼쪽으로 이동하는 경우를 비교
        min_left_right = min(min_left_right, idx + idx + len(name) - next_idx)

    answer += min_left_right
    return answer


print(solution("JAAOEN"))

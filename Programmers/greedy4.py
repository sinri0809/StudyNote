# greedy lv3 ์กฐ์ด์คํฑ ๐บ


def solution(name):
    answer = 0
    min_left_right = len(name)
    a = ord("A")
    z = ord("Z")
    next_idx = 0
    for idx, char in enumerate(name):
        answer += min(ord(char)-a, z-ord(char)+1)
        
        next_idx = idx + 1 # ๋ฐ๋ก ์์ผ๋ก ๊ฐ๋,
        while next_idx < len(name) and name[next_idx] == "A": # A๊ฐ ์๋ ๋ถ๋ถ์ผ๋ก ๊ฐ ๋,
            next_idx += 1
        
        # ํ ๋ฐฉํฅ์ผ๋ก๋ง ์ด๋ํ๋ ๊ฒฝ์ฐ์ ์ค๋ฅธ์ชฝ์ผ๋ก ์ด๋ํ๋ค๊ฐ ์ผ์ชฝ์ผ๋ก ์ด๋ํ๋ ๊ฒฝ์ฐ๋ฅผ ๋น๊ต
        min_left_right = min(min_left_right, idx + idx + len(name) - next_idx)

    answer += min_left_right
    return answer


print(solution("JAAOEN"))

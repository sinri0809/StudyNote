# hash lv2 2번째 풀이
# 전화번호 목록

input1 = ["119", "97674223", "1195524421"]
# input1 = ["123","456","789"]


# 어떤 번호가 다른 번호의 접두어인 경우가 있으면 false
def solution(phone_book):
    phone_book.sort()

    # for i in range(len(phone_book)):
    #     start = phone_book[i]
    #     for j in range(i+1, len(phone_book)):
    #         if phone_book[j].startswith(start):
    #             return False

    for i, j in zip(phone_book, phone_book[1:]):
        if j.startswith(i):
            print(f"{j}is start with{i}")
            return False
    return True
    
    
print(solution(input1))
# hash를 이용하여 푸는 방법을 생각해 볼 것.

# ❤solution
# 전화번호 목록
input1 = ["119", "97674223", "1195524421"]


# 한 번호가 다른 번호의 접두어가 되면 false
def solution(phone_book):
    phone_book.sort()
    print(phone_book)
    for phone1, phone2 in zip(phone_book, phone_book[1:]):
        print(phone1, phone2)
        if phone2.startswith(phone1):
            print(phone1)
    
    # for i in range(len(phone_book)):
    #     for j in range(i+1, len(phone_book)):
    #         if phone_book[j][:len(phone_book[i])] == phone_book[i]:
    #             return False
    # return True
            


print(solution(input1))

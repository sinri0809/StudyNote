# ex 3-1
N = int(input()) * 10
print("N: ", N)
count = 0
N_2 = N

lst = [500, 100, 50, 10]
for i in lst:
    count += N_2 // i
    print(i, "원", (N_2 //i), "개")
    # noinspection PyRedeclaration
    N_2 = N % i
    
print(count)

# 그리디 알고리즘 문제에서 최소한의 아이디어를 떠올리고
# 이의 정당성을 검토할 수 있어야 한다.

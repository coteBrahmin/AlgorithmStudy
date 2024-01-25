import sys

N, M = map(int, sys.stdin.readline().split())
baskets = [i for i in range(1, N + 1)] #바구니 번호 리스트 1,2,3,4,5

#바구니 역순으로 만들기 위한 for 문
#복사한 리스트. 해당하는 슬라이싱 범위에 역순으로 바꾼 바구니의 값을 할당
#깨달음) 슬라이싱할 때 인덱스 -1을 하고 안하고를 잘 생각해야 한다!

for i in range(1, M+1):
    x, y = map(int, sys.stdin.readline().split())
    baskets[x-1:y] = reversed(baskets[x-1:y])

print(*baskets)


########################
# import sys

# N, M = map(int, sys.stdin.readline().split())
# baskets = [i for i in range(1, N + 1)] #바구니 번호 리스트 1,2,3,4,5

# #바구니 역순으로 만들기 위한 for 문
# #복사한 리스트. 해당하는 슬라이싱 범위에 역순으로 바꾼 바구니의 값을 할당
# #깨달음) 슬라이싱할 때 인덱스 -1을 하고 안하고를 잘 생각해야 한다!

# for i in range(1, M+1):
#     x, y = map(int, sys.stdin.readline().split())
#     new = baskets
#     new[x-1:y] = reversed(baskets[x-1:y])

# print(*new)

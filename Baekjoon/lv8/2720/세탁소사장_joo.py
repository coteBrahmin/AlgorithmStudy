# 메모리: 33376 KB, 시간: 40 ms
#쿼터 - 25센트 / 다임 - 10센트 / 니켈 5센트 / 페니 1센트
#파이썬 % 나머지 연산자
#파이썬 // 몫 연산자


import sys, math
T = int(sys.stdin.readline())

for _ in range(T):
    total = int(sys.stdin.readline())
    Q = total // 25
    D = (total - Q*25)// 10
    N = (total-Q*25 -D*10)//5
    P = (total-Q*25-D*10-N*5)//1
    print(Q, D, N, P)
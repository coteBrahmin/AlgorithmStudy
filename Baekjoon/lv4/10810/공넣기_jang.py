import sys
n, m = map(int, sys.stdin.readline().split())
baskets = [0] * n
for i in range(m):
    s, e, ball = map(int, sys.stdin.readline().split())
    for a in range(s - 1, e):
        baskets[a] = ball
print(*baskets)

# 초기값 0인 리스트 만들기
# for문 돌면서 m번 입력값 받기
# 시작지점 s, 끝지점 e, 공 번호 ball
# 이중 for문으로 바구니 리스트에서 시작지점~끝지점까지 range 두고 공번호 넣어주기
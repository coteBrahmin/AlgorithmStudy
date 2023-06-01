import sys
n, m = map(int, sys.stdin.readline().split())
# 처음 상태의 바구니
baskets = [0] * n
for a in range(n):
    baskets[a] = a + 1
# 바구니 바꾸기
for b in range(m):
    i, j = map(int, sys.stdin.readline().split())
    change_b = []
    for c in range(i - 1, j):
        change_b.append(baskets[c])
    change_b.reverse()
    baskets[i - 1:j] = change_b

print(*baskets)

# 뒤집을 바구니의 범위를 이중for문에서 새로운 리스트로 만들어준 후, 해당 for문을 빠져나온 뒤 reverse로 뒤집어준다.
# 기존 리스트를 슬라이싱 해 뒤집어준 리스트를 할당해준다.
import sys
n, m = map(int, sys.stdin.readline().split())
baskets = [0] * n
save = 0

for a in range(n):
    baskets[a] = a + 1
    
for b in range(m):
    i, j = map(int, sys.stdin.readline().split())
    save = baskets[i-1]
    baskets[i-1] = baskets[j-1]
    baskets[j-1] = save

print(*baskets)

# 공을 서로 교환해야 하는데 i번째에 바로 대입해버리면 그 다음 j번째는 제대로 값을 할당받을 수 없음
# 따라서 변수에 따로 빼놓고 할당한다.
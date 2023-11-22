#memory 31120kb, time 148ms
import sys
N = int(sys.stdin.readline())
ans = 0
#수행 횟수는 시그마i + 시그마i-1 + ... + 시그마1
#시그마 공식을 통해 i값은 for문으로 순회
for i in range(0,N-1):
    ans += i*(i+1)//2
print(ans)
print(3)
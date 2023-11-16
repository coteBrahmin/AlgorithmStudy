# 메모리: 31256 KB, 시간: 48 ms
import sys

N = int(sys.stdin.readline())

#초기 한 변의 점의 개수는 2
length = 2

for _ in range(N):
    length = length + length - 1
    
result = length * length #총 점의 개수를 계산
print(result)
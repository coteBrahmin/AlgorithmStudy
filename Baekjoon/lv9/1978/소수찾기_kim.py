#memory 31120kb, time 40ms
import sys
N = int(sys.stdin.readline())
nums = list(map(int,sys.stdin.readline().split()))
count = N
for num in nums:
    if num == 1: count -= 1
    #소수는 1과 자기자신만을 약수로 하니까 탐색 범위를 2부터 자기자신-1로 지정
    for i in range(2,num):
        if num % i == 0:
            count -= 1
            break
        else: continue
print(count)
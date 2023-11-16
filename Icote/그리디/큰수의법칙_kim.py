import sys
N,M,K = map(int,sys.stdin.readline().split())
array = list(map(int,sys.stdin.readline().rstrip().split()))
Kcount = 3
ans = 0
#배열을 내림차순으로 sort한 뒤, K값을 체크해 가면서 가장 큰 수들로 합을 구성
array.sort(reverse=True)
for i in range(M):
    if Kcount == 0:
        ans += array[1]
        Kcount = 3
    else:
        ans += array[0]
        Kcount -= 1
print(ans)
import sys
N,K = map(int,sys.stdin.readline().split())
temp = N
ans = 0
#연산 횟수가 정해져있지 않으므로 while문을 썼다. 
while temp != 1:
    #K로 나누어 떨어지면 나누기
    if temp%K == 0:
        temp /= K
        ans += 1
    #K로 나눠떨어지지 않으면 1을 빼기    
    else:
        temp -= 1
        ans += 1
print(ans)

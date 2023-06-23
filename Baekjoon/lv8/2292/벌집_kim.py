#메모리 31256kb, 시간 56ms
import sys
N = int(sys.stdin.readline())
#한바퀴를 돌고 그 아래칸으로 넘어가는 지점을 각 항으로 하는 수열 AN
#직전 항에서 6의 배수만큼 증가한다 
#첫째항
beforeAN = 2
#n번째 
ans = 1
for n in range(1, N + 2):
    if N < beforeAN:
        print(ans)
        break
    else:
        AN = beforeAN + 6*(n-1)
        beforeAN = AN
        ans = n
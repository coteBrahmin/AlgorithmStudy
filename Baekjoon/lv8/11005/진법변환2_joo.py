# 메모리: 31388 KB, 시간: 48 ms
import sys
N, B = map(int, sys.stdin.readline().split())
ans = []

#B로 나눈 몫의 값인 N,
#N이 0보다 작아지면 작업을 종료해야 한다.
while N> 0:
    # N을 B로 나눈 나머지를 res에 저장
    res = N % B
    #만약 res가 10이상 35이하라면 ans에 알파벳 대문자로 변환하여 append
    if 10 <= res <= 35:
        ans.append(chr(55 + res))
    else:
        #아니라면 문자열로 변환하여 append
        ans.append(str(res))
    #그리고 N을 B로 나눈 몫을 다시 N으로 계산한다.
    N //= B
    print(N)

#ans를 역순으로 정리하여, 상위 자릿수부터 출력되도록 출력형식을 맞춰서 출력한다
ans.reverse()
print(''.join(ans))
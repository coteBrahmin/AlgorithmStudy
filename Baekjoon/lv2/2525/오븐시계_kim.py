H,M = map(int,input().split())
P = int(input())
#P를 시간 및 분 단위로 만들기
Ph = P//60
Pm = P%60
#종료 시간 계산
newH = H+Ph
newM = M+Pm
#분이 59보다 클 때 분-60 and 시간 +1
if newM>59:
    newH = newH+1
    newM = newM-60
    #시간이 24보다 클 때
    if newH>23: print(f"{newH-24} {newM}")
    else: print(f"{newH} {newM}")
#분이 59보다 작을 때
else:
    #시간이 24보다 클 때
    if newH>23: print(f"{newH-24} {newM}")
    else: print(f"{newH} {newM}")
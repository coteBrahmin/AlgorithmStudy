#memory 31120kb, time 56ms
import sys
A1,A0 = map(int,sys.stdin.readline().split())
C = int(sys.stdin.readline())
N = int(sys.stdin.readline())

Fn = A1*N + A0
if Fn <= C * N and A1<=C: 
    #조건에서 좌변과 우변은 모두 1차함수이기 때문에 기울기에 따라 교점 발생 시 O(N) 불만족
    #그래서 만족하려면 좌변 기울기가 우변보다 같거나 작아야됨
    print(1)
else :
    print(0)
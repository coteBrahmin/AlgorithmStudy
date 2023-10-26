#memory 35060kb, time 100ms
import sys
N = int(sys.stdin.readline())
#각 점의 좌표에서 x값끼리 모은 리스트와 y값끼리 모은 리스트를 만든다.
x = []
y = []
for i in range(N):
    dot = list(map(int,sys.stdin.readline().split()))
    x.append(dot[0])
    y.append(dot[1])
#max-min이 만들어지는 사각형의 가로세로변이 된다.
print((max(x)-min(x))*(max(y)-min(y)))
#memory 31120kb, time 40ms
import sys
dots = [list(map(int,sys.stdin.readline().split())) for _ in range(3)]
#각 좌표들의 x값끼리, y값끼리 들어간 리스트를 만든다. 
x = []
y = []
ans = []
for i in range(3):
    x.append(dots[i][0])
    y.append(dots[i][1])
#직사각형이라면 반드시 2개의 같은 x값과 y값이 필요함. 
#min에 해당하는 x값이 2개면 max에 해당하는 x값이 1개 더 필요하므로 
if x.count(min(x)) == 2: ans.append(max(x))
else: ans.append(min(x))
#같은 방식으로 y도 추가
if y.count(min(y)) == 2: ans.append(max(y))
else: ans.append(min(y))
print(*ans)
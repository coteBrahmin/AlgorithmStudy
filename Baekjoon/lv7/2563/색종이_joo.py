#메모리: 31256 KB, 시간: 44 ms
import sys
T = int(sys.stdin.readline())
paper =[[0]*100 for i in range(100)] #가로100/세로 100인 도화지


for _ in range(T):
    x, y = map(int, sys.stdin.readline().split())

#색종이의 가로와 세로의 길이는 각각 10이기 때문에 도화지에서 해당하는 좌표의 값을 1로 설정한다.
    for i in range(x, x+10): #가로
        for j in range(y, y+10): #세로
            paper[i][j] = 1
#그리고 전체 넓이, 1로 설정된 영역의 개수를 모든 더해 출력한다.
area = 0
for i in range(100):
    for j in range(100):
        if paper[i][j] == 1:
            area+=1
print(area)
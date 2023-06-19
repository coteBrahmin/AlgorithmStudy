# 메모리: 31256 KB, 시간: 48 ms
import sys

#5줄의 인풋값을 matrix에 담아준다.
matrix = [list(sys.stdin.readline().strip()) for i in range(5)]

ans = []
column = 0

#최대 15개의 글자들, 그리고 줄마다 다를 수 있기 때문에 15만큼의 반복문을 설정
#그리고 row는 5줄이기 때문에 이중 for문 설정
for c in range(15):
    for r in range(5):
        column = len(matrix[r]) 
        #현재 열이 해당 줄의 길이(column) 보다 작은 경우
        #matrix에 해당 값을 넣어준다.
        if c < column:
            ans.append(matrix[r][c])

#세로로 읽은 문자열 출력
print(*ans,sep="")
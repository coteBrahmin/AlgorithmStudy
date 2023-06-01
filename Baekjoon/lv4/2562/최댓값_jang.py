import sys
num = []
for i in range(9):
    num.append(int(sys.stdin.readline().strip()))

print(max(num))
print(num.index(max(num)) + 1)

# 입력값 개수 정해져 있으므로 for문 range 고정
# for문 돌면서 입력값 받아 리스트에 넣기
# max()함수 이용해 최댓값 도출,
# 몇번 째인지는 1부터 시작하기 때문에 인덱스 + 1
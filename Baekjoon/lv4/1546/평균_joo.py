import sys

#입력값을 받아온다. 
N = int(sys.stdin.readline())
score = list(map(int, sys.stdin.readline().split()))
#그리고 최대 점수를 M으로 할당하였습니다. 
M = max(score)
sum = 0

#새로운 점수 리스트를 만들어 새로운 점수를 반복문을 통해 구해서, 합을 출력합니다. 
for i in range(0, N):
    score2= score
    score2[i] = score2[i] / M * 100
    sum += score2[i]

print(sum / len(score))
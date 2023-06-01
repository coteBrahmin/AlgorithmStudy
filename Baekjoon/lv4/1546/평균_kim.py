#과목 수
count = int(input())
#과목별 점수 리스트
scores = list(map(int,input().split()))
#조작할 새로운 점수 리스트
newScores = []
#계산한 대로 조작한 점수를 새 리스트에 추가
for score in scores:
    newScores.append(score/max(scores)*100)
#평균은 원소 전체 더해서 원소개수로 나누기    
print(sum(newScores)/len(newScores))
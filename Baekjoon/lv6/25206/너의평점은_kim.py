#메모리 31256kb, 시간 40ms
import sys
#학점 총합 credits
credits = 0
#학점 * 평점의 총합 creditXscore
creditXscore = 0
#평점을 숫자로 환산한 점수표 딕셔너리
dic = {'A+':4.5, 'A0':4.0, 'B+':3.5, 'B0':3.0, 'C+':2.5, 'C0':2.0, 'D+':1.5, 'D0':1.0, 'F':0.0}

for _ in range(20):
    lecture, credit, score = list(map(str,sys.stdin.readline().split()))
    #평점이 P인 것은 계산에서 제외
    if score == 'P': continue
    #문자열을 실수타입으로 변경
    credits += float(credit)
    creditXscore += float(credit)*dic[score]
#이것도 소수점 6째자리까지 표기해야 하므로 format함수 사용, 
# format함수는 str이여야 하기 때문에 포맷팅
print(f"{format(creditXscore/credits,'.6f')}")
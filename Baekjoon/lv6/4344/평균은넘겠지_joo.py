#메모리: 31256 KB, 시간: 48 ms
import sys

C = int(sys.stdin.readline())

for _ in range(C):
    scores = list(map(int, sys.stdin.readline().split()))
    N = scores.pop(0) #학생수
    sum = 0
    for i in range(N):
        sum += scores[i] #총합
        avg = sum / N #평균
        avg_sum = 0
    
    #평균을 넘는 학생의 경우에는 학생수 +1
    for j in range(N):
        if scores[j] > avg: avg_sum += 1

    print(f"{avg_sum/N * 100:.3f}" , "%", sep="")

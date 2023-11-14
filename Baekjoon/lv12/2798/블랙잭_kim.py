#memory 43924kb, time 144ms
import sys
N,M = map(int,sys.stdin.readline().split())
cards = list(map(int,sys.stdin.readline().split()))
sums = {}
#중복을 제외하고 카드에서 3장을 고르는 경우 
for i in range(N-2):
    for j in range(i+1,N-1):
        for k in range(j+1,N):
            #카드 3장을 더한 값이 M보다 작으면, {M-더한값: 더한값} 
            if M-(cards[i]+cards[j]+cards[k]) >= 0 :
                sums[M-(cards[i]+cards[j]+cards[k])] = cards[i]+cards[j]+cards[k]
#M-더한값이 가장 작은 경우의 더한값 출력
print(sums[min(sums.keys())])
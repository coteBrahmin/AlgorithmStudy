N,M = map(int,input().split())
#1번부터 N번까지 바구니 리스트
bucket = list(range(1,N+1))
for _ in range(M):
    i,j = map(int,input().split())
    #구글링해서 위치 바꾸기 찾음.. 전에 파이썬 선생님이 swap에 대해 말한 적 있음
    bucket[i-1], bucket[j-1] = bucket[j-1], bucket[i-1]
print(' '.join(map(str,bucket)))
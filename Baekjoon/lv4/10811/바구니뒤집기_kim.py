N,M = map(int,input().split())
#1번부터 N번까지 번호가 붙어있는 바구니 리스트
buckets = list(range(1,N+1))
#i번부터 j번까지 순서를 바꿀 바구니 리스트
change = []
for _ in range(M):
    i,j = map(int,input().split())
    #바구니의 인덱스는 바구니번호보다 1씩 작으므로 슬라이스를 할려면
    change = buckets[i-1:j]
    #원래 바구니 리스트에서 일단 삭제
    del buckets[i-1:j]
    #i-1번째에다가 슬라이싱한 change리스트를 처음부터 순서대로 넣으면, 
    #자연스럽게 리버스가 되어 들어가게 된다 (삽질하다가 우연히 발견 후 디버깅 해봄)
    for k in change:
        buckets.insert(i-1,k)
print(' '.join(map(str,buckets)))
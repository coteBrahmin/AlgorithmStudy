N,M = map(int,input().split())
#일단 공이 안들어가있는 바구니 리스트
bucket = [0]*N
for _ in range(M):
    i,j,k = map(int,input().split())
    #바구니의 인덱스는 바구니 번호보다 1 작으므로
    for put in range(i-1,j):
        #put번째 바구니에 k번 공을 넣는다
        bucket[put] = k
#리스트를 문자열로 바꿔 출력하는 함수 join, 숫자로 된 리스트를 문자열로 바꾸는 함수 map
print(' '.join(map(str,bucket)))
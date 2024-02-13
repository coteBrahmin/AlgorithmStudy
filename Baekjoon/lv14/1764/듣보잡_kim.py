import sys
N,M = map(int,sys.stdin.readline().split())
heard_dict = {}
for i in range(N):
    heared = sys.stdin.readline().rstrip()
    heard_dict[heared] = 0
result = {}
for j in range(M):
    saw = sys.stdin.readline().rstrip()
    #듣도 + 보도 이려면 듣도는 반드시 포함이어야 한다.
    if saw in heard_dict:
        result[j] = saw
result = sorted(result.values())
print(len(result))
for k in range(len(result)):
    print(result[k])

#이름을 사전정렬해야 해서 values list로 만들고 정렬했는데, 
#dict 내에서 정렬하는 방법 없을까... 
    
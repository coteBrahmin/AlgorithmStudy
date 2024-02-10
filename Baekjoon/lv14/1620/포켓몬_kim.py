import sys
N,M = map(int,sys.stdin.readline().split())
dogam = {}
for i in range(1,N+1):
    poketmon = sys.stdin.readline().rstrip()
    dogam[str(i)] = poketmon
dogam_reverse = {v:k for k,v in dogam.items()}
for j in range(M):
    input = sys.stdin.readline().rstrip()
    if input in dogam:
        print(dogam[input])
    if input in dogam_reverse:
        print(dogam_reverse[input])
        #print([k for k, v in dogam.items() if v == input][0])

#value로 key를 찾는 과정을 리스트탐색으로 하면 O(n)이라서 그런듯
#리버스 딕셔너리를 만들어 O(1)을 2회 하는 것이 나은 것이다. 
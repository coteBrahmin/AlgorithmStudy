import sys
N = int(sys.stdin.readline())
workers = {}
for i in range(N):
    data = sys.stdin.readline().split()
    name = data[0]
    check = data[1]
    workers[name] = check
result = []
for j in workers:
    if workers[j] == 'enter':
        result.append(j)
result.sort(reverse=True)
for name in result:
    print(name)

#map으로 입력받는건 정수일때만 가능한듯.. map함수에 대해 더 공부 필요
#입력을 여러줄 받을 때 꼭 한번에 다 받을 필요없다. 들어오는 입력 줄 개수만 맞으면 각각 다른 블록에서 입력받아도 됨
#딕셔너리의 keys()등은 참조할 수 없음 print(dict.keys()[i]) 불가
#sorted(dict.keys()) 를 변수에 할당하면 리스트로 할당된다. 

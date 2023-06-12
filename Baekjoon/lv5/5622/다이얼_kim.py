str = list(input())
#전화번호에 해당하는 글자들을 묶어서 이차원 리스트 생성,
#인덱스를 맞추기 위해서 [0],[1]을 임의로 넣음
group = [[0],[1],['A','B','C'],['D','E','F'],['G','H','I'],['J','K','L'],['M','N','O'],['P','Q','R','S'],['T','U','V'],['W','X','Y','Z']]
ans = 0
for i in str:
    #입력받은 str의 글자가 어느 그룹에 속해 있는지 탐색
    for j in range(10):
        if i in group[j]:
            #글자가 속한 group의 인덱스+1초 만큼 걸리고, 그것을 누적 합산 
            ans = ans + (group.index(group[j])+1)
        else: continue
print(ans)
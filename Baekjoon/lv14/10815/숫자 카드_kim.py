import sys
N = int(sys.stdin.readline().rstrip())
nums = list(map(int,sys.stdin.readline().split()))
M = int(sys.stdin.readline().rstrip())
nums2 = list(map(int,sys.stdin.readline().split()))
m_nums = {}
for i in range(N):
    m_nums[nums[i]] = 0

for j in range(M):
    if nums2[j] in m_nums:
        print(1, end=' ')
    else:
        print(0, end=' ')

#for i in list와, for i in dict 의 차이, 그리고 
#for i in list와, for i in range(len(list)) 에 무슨 차이가 있는지 실험해볼것
#이진 검색으로 구현하는 방법도 있는데 자료구조 연습하는 겸 공부할 것

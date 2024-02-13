import sys
S = sys.stdin.readline().rstrip()
s_dict={}
for i in range(len(S)+1):
    for j in range(i+1,len(S)+1):
        if S[i:j] in s_dict:
            s_dict[S[i:j]] += 1
        else:
            s_dict[S[i:j]] = 1
print(len(s_dict))

#갓토에버 코테에 나왔던 토픽이다. 
#문자열의 인덱싱과 슬라이싱을 자유롭게 활용할 수 있어야 한다.
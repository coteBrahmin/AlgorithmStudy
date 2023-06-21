#메모리 31388kb, 시간 48ms
import sys
N,B = map(str,sys.stdin.readline().split())
#10자리 넘어가는 수 변환기 딕셔너리
dic = {'A':10, 'B':11, 'C':12, 'D':13, 'E':14, 'F':15, 'G':16, 'H':17, 'I':18, 'J':19, 'K':20, 'L':21, 'M':22, 'N':23, 'O':24, 'P':25, 'Q':26, 'R':27, 'S':28, 'T':29, 'U':30, 'V':31, 'W':32, 'X':33, 'Y':34, 'Z':35}
convertN = []
for j in range(len(N)):
    #10자리가 넘어가면 변환기를 통한 계산
    if N[j] in dic.keys(): convertN.append(dic[N[j]]*(int(B)**(len(N)-1-j)))
    #10자리 이내이면 바로 계산
    else: convertN.append(int(N[j])*(int(B)**(len(N)-1-j)))
print(sum(convertN))

# B진법을 10진법으로 변환하려면 
# 각 자리수 * B^(수의 길이-1)

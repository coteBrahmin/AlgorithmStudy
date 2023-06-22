#첫 번째 방법
#메모리 31388kb, 시간 44ms
import sys
N,B = map(int,sys.stdin.readline().split())
#자릿수 변환을 또 해야되는데 이번에는 숫자가 key가 되어야 밸류에 접근 가능해서 딕셔너리 쌍을 뒤집음
dic = {10:'A', 11:'B', 12:'C', 13:'D', 14:'E', 15:'F', 16:'G', 17:'H', 18:'I', 19:'J', 20:'K', 21:'L', 22:'M', 23:'N', 24:'O', 25:'P', 26:'Q', 27:'R', 28:'S', 29:'T', 30:'U', 31:'V', 32:'W', 33:'X', 34:'Y', 35:'Z'}
convertN = []
#진법 계산을 몰라서 구글링.. 바꾸려고 하는 진수로 나누면서 나머지 있을때 리스트에 추가하고 
#한번 나눌 때마다 N은 나눈 몫으로 바꿔주기
while N != 0:
    convertN.append(N%B)
    N = N//B
for i in range(len(convertN)):
    if convertN[i] in dic.keys(): convertN[i] = dic[convertN[i]]
    else: continue
#첫 번째로 나눌 때의 나머지가 1의자리에서부터 구성되기 때문에 리스트를 뒤집어줌
convertN.reverse()
print(*convertN, sep='')

#두 번째 방법
#메모리 31256kb, 시간 76ms
import sys
N,B = map(int,sys.stdin.readline().split())
#문자열의 인덱스를 통해 접근하는 방법도 있음 (구글에서 발견해서 시도해보기로 함)
dic = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
convertN = []
while N != 0:
    convertN.append(N%B)
    N = N//B
for i in range(len(convertN)):
    convertN[i] = dic[convertN[i]]
convertN.reverse()
print(*convertN, sep='')

#결과적으로 코드는 두번째 방법이 단순한데 효율성은 딕셔너리를 쓰는 게 나았음
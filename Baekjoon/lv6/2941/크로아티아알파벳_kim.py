#메모리 31256kb, 시간 44ms
import sys
str = sys.stdin.readline().strip()
#크로아티아 알파벳을 key, 그 개수를 value로 한 딕셔너리 
dic = {'c=':0, 'c-':0, 'dz=':0, 'd-':0, 'lj':0, 'nj':0, 's=':0, 'z=':0}

#딕셔너리 밸류 개수 + 남은 문자 개수를 통해 최종 개수 구하려고 함
for key in dic.keys():
    if key in str:
        #같은 문자가 여러번 있을 경우를 위해 str안에서 그 문자 몇개인지 체크
        #첫 시도때 같은 문자 체크 작업을 안 해서 삽질함.. 
        dic[key] = str.count(key)
        #그 문자를 콤마로 대체 
        str = str.replace(f'{key}',',')
    else: continue

#남은 문자에서 콤마를 없애줘야 len(str)이 남은 글자 길이가 됨
str = str.replace(',','')
print(len(str)+sum(dic.values()))


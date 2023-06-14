#메모리 40044kb, 시간 196ms
str = list(input().upper())
dic = {}
#입력받은 문자를 key로 하고 그 문자 개수를 value로 하는 딕셔너리 생성
for word in str:
    dic[word] = dic.get(word,0) +1
ans = ''
for i in dic.keys():
    #value값이 최대인 key를 ans에 추가
    if dic.get(i) == max(list(dic.values())) :  ans += i
    else: continue
#key가 2개 이상이면 ?
if len(ans) >1 : print('?')
else: print(ans)
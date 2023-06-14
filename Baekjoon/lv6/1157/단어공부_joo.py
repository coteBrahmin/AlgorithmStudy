#메모리: 33212 KB, 시간: 204 ms

import sys
word = sys.stdin.readline().strip().upper()
word_dict = {}

#문자가 단어 딕셔너리에 포함되어 있다면 값 1추가 아니라면 그냥 1
for char in word:
    if char in word_dict:
        word_dict[char]+=1
    else:
        word_dict[char] =1

#최대값과 최대값이 나오게 하는 문자 max_chars - 딕셔너리의 키와 값을 모두 가져오는 items()를 이용
max_value = max(word_dict.values())
max_chars = [char for char, count in word_dict.items() if count== max_value]

if list(word_dict.values()).count(max_value) >1 :
    print("?")
else: print(*max_chars)





#참고) 
# 시간이 너무 오래 걸린다.
# if char.isalpha():알파벳 여부 확인 isalpha
#from collections import defaultdict를 쓸 수도 있다. - 알파벳 개수를 세주는 딕셔너리 
# sorted_dict = sorted(word_dict.items(), key=lambda x:x[1], reverse=True) #파이썬 람다함수를 이용해 값을 기준 정렬 키와 값이 같이 출력됨



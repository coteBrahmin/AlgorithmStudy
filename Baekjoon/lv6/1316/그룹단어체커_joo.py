#메모리: 31256 KB, 시간: 44 ms

N = int(input().strip())
num = N

#만약 첫번째 단어가 아니고(i!=0), 단어가 단어의 set안에 이미 있고 이전 단어와 같지 않다면 
#그룹 단어가 아니라고 판단한다. 
#그룹단어라면 set에 단어를 추가한다. 

#그룹단어가 아니라면 단어의 개수에서 1을 빼준다.
for _ in range(N):
    word = list(input().strip())
    word_set = set()
    group_word = True
    
    for i in range(len(word)):
        if i!=0 and word[i] in word_set and word[i-1] != word[i]:
            group_word = False
        else:
            word_set.add(word[i])

    if not group_word:
        num -= 1

print(num)


##그룹 단어이 아닐 경우) 중복된 알파벳이면서도 그전 알파벳과 다른 경우 
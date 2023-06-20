#메모리 31256kb, 시간 52ms
import sys
words = []
for _ in range(5):
    word = list(sys.stdin.readline().strip())
    #모든 리스트의 인덱스를 15개로 만들기 위해 부족하면 *을 추가 
    while len(word) < 15:
        word.append('*')
    words.append(word)
new_words = ''
for i in range(15):
    #i번째 줄을 세로로 읽은 글자
    new_word = []
    for j in range(5):
        # '*'이 있는 경우 건너 뛰고 읽은 글자를 new_word에 추가
        if words[j][i] == '*': continue
        else: new_word.append(words[j][i])
    #세로로 읽은 글자들을 이어 붙인 최종 결과
    new_words += ''.join(w for w in new_word)
print(new_words.strip())
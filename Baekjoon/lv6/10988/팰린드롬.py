#31256KB, 40ms
#리스트로 input을 받아오고,
#뒤집었을 때와 같은지 확인합니다.

word = list(input())

if word == word[::-1]:
    print(1)
else: print(0)


import sys
T = int(sys.stdin.readline())



#테스트 케이스의 개수만큼 for문을 실행한다.
#반복 횟수 num,  문자열을 letter로 할당했다.
#그리고 문자열 리스트의 각각의 원소들을 num 번 출력한다. 
#여기서 end =""로 해주어서 출력형식을 맞춘다.

### 개행 추가를 해주어야 다음 문장을 읽어옴에 주의하라!

for i in range(1, T+1):
    num, letter = sys.stdin.readline().split()
    letter = list(letter)
    for j in range(0, len(letter)):
        print(letter[j]*int(num), end="")
    print()
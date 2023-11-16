#메모리: 31256 KB, 시간: 44 ms
import sys

alphabet = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=","z="]
letter = list(sys.stdin.readline().strip())

num = 0
i= 0

#1)
#i가 단어의 길이를 넘지 않고, 3자리를 슬라이싱했을때 dz=와 같다면 
#크로아티아 알파벳 개수 num + 1
#그리고 포인터 i를 3만큼 더한다.

#2)2자리를 슬라이싱 했을때 알파벳 리스트안에 있다면, num+1 그리고 i+2를 해준다.
#3) 아니라면 그냥 알파벳이므로 num과 i에 1을 더해준다.
while i < len(letter):
    if i + 2 < len(letter) and "".join(letter[i:i+3]) == "dz=":
        num += 1
        i += 3
    elif "".join(letter[i:i+2]) in alphabet:
        num +=1
        i += 2
    else:
        num+=1
        i+=1


print(num)
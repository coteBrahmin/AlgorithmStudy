import sys

# 파이썬 알파벳 전체 출력하는 방법이 궁금하다.
# from string import ascii_uppercase

alphabet_dict = {"A":3, "B":3, "C":3, "D":4, "E":4, "F":4,
                 "G":5, "H":5, "I":5, "J":6, "K":6, "L":6,
                 "M":7, "N":7, "O":7, "P":8, "Q":8, "R":8,
                 "S":8, "T":9, "U":9, "V":9, "W":10, "X":10,
                 "Y":10, "Z":10}

#알파벳을 딕셔너리 형태로 만든다.
#인풋값을 리스트로 받아온다. 
dial = list(sys.stdin.readline().strip())
sum = 0

#for 문을 통해 알파벳의 키값을 통해 value값을 더하는 작업을 반복한다. 
for i in range(0, len(dial)):
    sum += alphabet_dict.get(dial[i])

print(sum)


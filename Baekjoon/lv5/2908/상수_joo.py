#파이썬 구분자.join()

#인풋값 두 수를 A,B에 할당한다. 예시) A = 734
A, B = input().split()
lsA = "".join(list(A)[::-1])
lsB= "".join(list(B)[::-1])

# print(list(A)[::-1]) 를 하면 ['4', '3', '7']이 되고 
#앞에 join을 붙이면 역수인 437
# 최댓값을 출력합니다.
print(max(lsA,lsB))
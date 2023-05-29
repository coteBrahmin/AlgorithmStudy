# 방법 1
# 1. input이 줄바꿈하여 들어오기 때문에 두 번 받아서 할당하고, int()함수로 형변환해준다.
# 2. a를 b의 각 자리수와 곱하기 위해 b를 문자열로 형변환 한 후, map()함수로 각각 정수로 형변환 하여 변수 c,d,e에 할당한다.
# 3. 각각을 곱하여 출력한다.
a = int(input())
b = int(input())

c, d, e = map(int, str(b))

print(a*e)
print(a*d)
print(a*c)
print(a*b)


# 구글링해서 찾아본 방법
# a는 입력받아 정수형으로 형변환, b는 쪼갤거니까 문자열로 입력받기만 함.
a = int(input())
b = input()

# 문자열은 인덱싱이 가능하다.
# b의 각 자리를 정수형으로 형변환하여 a와 곱한다.
# 마지막 결과물은 a와 b를 곱한다.
c = a*int(b[2])
d = a*int(b[1])
e = a*int(b[0])
a1 = a*int(b)

# print문의 sep옵션으로 줄바꿈을 주어 각 변수 사이에 줄바꿈을 넣어준다.
print(c, d, e, a1, sep='\n')
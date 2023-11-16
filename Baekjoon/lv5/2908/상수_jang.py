a, b = map(str, input().split())

A = ''.join(list(reversed(a)))
B = ''.join(list(reversed(b)))

if int(A) > int(B):
    print(int(A))
else:
    print(int(B))

# 우선 입력값을 문자열로 받는다.
# reversed 함수로 문자열을 뒤집은 후 list로 형변환 한 뒤,
# join으로 각 요소를 합쳐 한 문자열로 만들어 A, B에 힐당한다.
# A, B를 정수형으로 형변환하여 크기를 비교하여 조건문으로 결과를 출력한다 
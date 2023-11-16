#인풋값 받아오기
x, y, z = map(int, input().split())

#3가지 경우가 모두 같을 떄, 다를때
#2가지가 같을 때를 나누어보았는데 비효율적이라고 생각합니다.
if x == y and y == z and x==z:
    print(10000+x*1000)
elif x !=y and y!=z and x!=z:
    print(max(x,y,z)*100)
elif x!=y and x==z :
    print(1000+x*100)
elif x==y and y!=z:
    print(1000+x*100)
else: print(1000+y*100)


#조건문을 더 간략하게 효율적으로 쓸 수 있었다. 
# A,B,C = map(int,input().split())
# #세 수가 모두 같은 경우
# if A == B and B == C: print(10000+1000*A)
# #두 수가 같은 경우
# elif A == B or A == C: print(1000+100*A)
# elif B == C: print(1000+100*B)
# #모두 다른 경우
# else:
#     print(max(A,B,C)*100)
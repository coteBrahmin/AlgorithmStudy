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
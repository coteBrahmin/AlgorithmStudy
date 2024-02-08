import sys
a,b = map(int,sys.stdin.readline().split())

def gcb(x,y):
    if x<y:
        x,y = y,x
    while y != 0:
        x %= y
        x,y = y,x
    return x

#최소공배수는 두 수를 곱한 뒤 최대공약수로 나눠주면 된다. 
print(a*b//gcb(a,b))
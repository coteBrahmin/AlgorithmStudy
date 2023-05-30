A,B,C = map(int,input().split())
#세 수가 모두 같은 경우
if A == B and B == C: print(10000+1000*A)
#두 수가 같은 경우
elif A == B or A == C: print(1000+100*A)
elif B == C: print(1000+100*B)
#모두 다른 경우
else:
    numlist = [A,B,C]
    numlist.sort()
    print(100*numlist[-1])


# #best code
# A,B,C = map(int,input().split())
# #세 수가 모두 같은 경우
# if A == B and B == C: print(10000+1000*A)
# #두 수가 같은 경우
# elif A == B or A == C: print(1000+100*A)
# elif B == C: print(1000+100*B)
# #모두 다른 경우
# else:
#     print(max(A,B,C)*100)
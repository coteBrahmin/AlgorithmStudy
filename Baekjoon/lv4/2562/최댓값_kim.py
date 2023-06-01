nums = []
for i in range(9):
    #한 줄씩 입력받은 수를 리스트에다 넣기
    N = int(input())
    nums.append(N)
#가장 큰 요소 찾는 함수 max
print(max(nums))
#그 값의 index는 0부터 세니까 +1해야 Nst number 
print(nums.index(max(nums))+1)
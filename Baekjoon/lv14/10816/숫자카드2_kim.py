import sys
N = int(sys.stdin.readline())
nums = list(map(int,sys.stdin.readline().split()))
M = int(sys.stdin.readline())
check = list(map(int,sys.stdin.readline().split()))
nums_dict = {}
for j in range(N):
    #1번째 시도 : nums_dict[nums[i]] = nums.count(nums[i])
    if nums[j] in nums_dict:
        nums_dict[nums[j]] += 1
    else:
        nums_dict[nums[j]] = 1

for i in range(M):
    if check[i] in nums_dict:
        print(nums_dict[check[i]], end=' ')
    else:
        print(0, end=' ')

#언뜻 생각해보면 1번째 방법이 한번에 딕셔너리를 완성하는 효율적? 방법 같아 보이지만
#list.count() 연산이 O(n)이기 때문에 dict 탐색인 O(1)회를 그 개수만큼 해주는 것이 빠르다.
        
nums.sort()

def binary_search (array,target):
    pointer_log = []
    pointer = array[len(array)//2]
    while pointer != target :
        if pointer > target:
            if pointer in pointer_log:
                return 0
            pointer_log.append(pointer)
            pointer = array[array.index(pointer) // 2]
        else:
            if pointer in pointer_log:
                return 0
            pointer_log.append(pointer)
            pointer = array[(array.index(pointer) + len(array)) // 2]
    return array.count(pointer)

for i in range(M):
    result = binary_search(nums,check[i])
    print(result, end=' ')

#숫자카드 1번에서 시도하지 못한 이진 검색 트리의 방법으로 시도를 해보았다. 
#이것도 시간초과가 나긴 했지만, 이진 검색 트리 연습을 한 것에 큰 의미가 있다. 
#리스트 연산 O(n)*1 > 이진 검색 트리 O(logn)*1 > 딕셔너리 O(1)*n 순으로 시간 복잡도가 작다. 
    
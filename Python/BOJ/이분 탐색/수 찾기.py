# 이분 탐색 알고리즘을 이용하여 해당 수가 있는지 체크 있으면 True, 없으면 False 반환

def binary_search(target, start, end): # 이분 탐색 구현
  while start <= end:
    mid = (start + end) // 2

    if numbers[mid] == target: # 찾는 수가 있으면 True
      return True
    elif numbers[mid] > target:
      end = mid - 1
    else:
      start = mid + 1
  
  return False # 없으면 False

n = int(input())
numbers = list(map(int, input().split()))

m = int(input())
x = list(map(int, input().split()))

numbers.sort() # 이분탐색 알고리즘을 적용하기 위해서는 정렬되어 있어야 하므로 정렬
for i in range(m):
  if binary_search(x[i], 0, n-1): # x의 요소들 하나씩 numbers에 있는지 없는지 체크
    print(1)
  else:
    print(0)

# 문제의 조건에 따라 좌표 압축을 진행하면 됨
# 주어진 배열을 오름차순 정렬하여 해당 요소의 인덱스가 좌표 압축 결과
# 이때 숫자들을 중복될 수 있으므로 set을 이용하여 중복을 제거하고 오름차순 정렬
# n의 범위가 10 ** 6이므로 단순히 index 메소드를 이용하여 요소를 찾으면 시간초과, 이때 index 메소드의 시간 복잡도는 O(n)
# # 이분탐색 알고리즘을 적용하여 해당 요소의 인덱스를 찾음

# import sys
# input = sys.stdin.readline

# def binary_search(target, start, end): # 이분탐색 알고리즘 구현
#   while start <= end:
#     mid = (start + end) // 2

#     if copy[mid] == target: # 해당 요소를 찾으면 인덱스 return
#       return mid

#     elif copy[mid] > target: # 해당 요소가 작으면 end 값 - 1
#       end = mid - 1
      
#     else: # 해당 요소가 크면 start값 + 1
#       start = mid + 1

# n = int(input())
# numbers = list(map(int, input().split()))

# copy = sorted(set(numbers)) # numbers의 중복을 제거하고 오름차순 정렬
# for i in range(n):
#   numbers[i] = binary_search(numbers[i], 0, len(copy) - 1) # 해당 요소의 인덱스 찾음

# print(*numbers)

# 해당 요소의 범위가 워낙 크기 때문에 이분탐색도 많은 시간 소요됨
# 딕셔너리를 통해 인덱스 검색, 딕셔너리 검색은 시간 복잡도 O(1)

import sys
input = sys.stdin.readline

n = int(input())
numbers = list(map(int, input().split()))

copy = sorted(set(numbers))
# location = dict(zip(copy, range(len(copy)))) # zip을 이용하여 copy와 인덱스를 묶고, dict으로 변환 즉, key는 copy 요소가 되고, value가 인덱스가됨
location = {copy[i] : i for i in range(len(copy))} # dict을 만들 때 위 방법 대신 이렇게 만들어도 됨

print(*[location[num] for num in numbers]) # numbers의 모든 요소를 순회하면서 location에 해당하는 value 값 찾음

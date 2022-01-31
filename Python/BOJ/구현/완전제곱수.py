# m, n 사이에 있는 완전 제곱수를 모두 찾으면 됨
# 일일이 찾는 것이 아닌 m, n의 제곱근 사이의 값들만 찾으면 됨
# # 즉 O(n) => O(logn)으로 줄일 수 있음
# import math
# # 수들을 입력 받으면서 바로 가공
# # m은 시작 값이므로 math 모듈의 ceil을 사용하여 올림수를 저장
# # n은 끝 값이므로 입력 받은 수의 제곱근 + 1 값을 저장
# m, n = math.ceil(int(input()) ** 0.5), int(int(input()) ** 0.5) + 1

# result = range(m, n) # range 함수를 이용하여 범위를 만듦
# if result: # result의 요소가 한개라도 있으면
#   print(sum(map(lambda x: x ** 2, result))) # sum과 map 함수를 이용하여 모든 요소 덧셈
#   print(result[0] ** 2) # 제일 작은 값 출력
# else: # result에 요소가 없으면 -1 출력
#   print(-1)

# functools 모듈의 reduce 함수 사용
# sum, map을 사용한 것보다 느림
import math
from functools import reduce

m, n = math.ceil(int(input()) ** 0.5), int(int(input()) ** 0.5) + 1

result = range(m, n)
if result:
  # reduce 함수를 사용하여 result의 모든 요소 덧셈
  print(reduce(lambda total, cur: total + cur ** 2, result, 0))
  print(result[0] ** 2)
else:
  print(-1)

# 로프를 병행로 연결했을 때 모든 로프는 w/k 만큼을 동일하게 들 수 있음
# 즉, 입력 받은 각 로프가 버틸 수 있는 최대 중량 리스트를 정렬하여
# 해당 요소 * 해당 요소부터 리스트 길이 중 제일 큰 것을 고르면 됨
# 예를 들어, [3, 10, 100, 500] 이라면 4개를 선택 했을 경우 최대 중량은 3*4, 3개를 선택 했을 경우 최대 중량은 10*3, ...
# 위 예시에서 500을 들 수 있는 로프를 한 개 고르면 최대 중량이 됨
# 몇 개의 로프를 골라서 최대 중량을 구하는 문제이므로 즉, 최대 중량을 구하기 위해 로프를 골라야 하므로 그리디 알고리즘 적용

import sys
input = sys.stdin.readline # 입력 받을 때는 항사 sys 사용할 것! 속도 차이가 엄청남..

n = int(input())

weight = []
for _ in range(n):
  weight.append(int(input()))

weight.sort()
result = 0
for i in range(len(weight)):
  tmp = weight[i] * (len(weight) - i) # 정렬된 리스트 모든 요소에서 최대 중량을 체크 
  if result < tmp: # 제일 큰 값을 result에 저장
    result = tmp

print(result) 

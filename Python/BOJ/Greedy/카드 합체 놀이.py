# 만들 수 있는 점수를 가장 작게 만들기 위해서는 가장 작은 두 수를 계속해서 더해 나가면 됨, 그리디 알고리즘 적용
# 이때 카드를 합체한 이후 계속 정렬되어 있어야 하기 때문에 우선순위 큐(heap)을 사용
# heap은 항상 정렬된 상태를 유지

import heapq

n, m = map(int, input().split())
numbers = list(map(int, input().split()))

heapq.heapify(numbers) # 입력받은 numbers 리스트를 heap으로 변환
while m > 0: # m번 카드 합체
  a = heapq.heappop(numbers) # 제일 작은 수 pop
  b = heapq.heappop(numbers) # 두번째로 작은 수 pop
  
  # 2번의 pop을 하여 덮어써야 하므로 다시 2번 push
  heapq.heappush(numbers, a+b)
  heapq.heappush(numbers, a+b)

  m -= 1

print(sum(numbers))

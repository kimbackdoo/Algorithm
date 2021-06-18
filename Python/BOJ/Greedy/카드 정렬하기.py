# 리스트를 선언하고 pop, append, sort 연산을 반복적으로 한 결과 시간초과
# 우선순위 큐인 heapq 사용, 우선순위 큐 : 들어간 순서에 상관없이 우선순위가 높은 데이터가 먼저 나오는 큐
# n의 범위가 1이상이고, 예를 들어, n=1일 경우 비교 횟수는 0

import heapq

n = int(input())

cards = []
for _ in range(n):
  cards.append(int(input()))

result = 0

heapq.heapify(cards) # 입력 받은 cards 리스트를 heap으로 변환
while len(cards) != 1: # 길이가 1일 때까지 반복
  # 첫번째, 2번째를 빼내서 result에 누적
  a = heapq.heappop(cards)
  b = heapq.heappop(cards)
  result += (a + b)
  heapq.heappush(cards, a + b) # 빼낸 a, b를 cards에 삽입, 이때 cards는 우선순위 큐이므로 삽입하면서 자동으로 정렬된다

print(result)

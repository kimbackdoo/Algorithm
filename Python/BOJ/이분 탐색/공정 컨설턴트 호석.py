# 단순히 n번 비교해서 탐색 -> 시간초과
# heap을 사용하여 push, pop 연산할 때 자동으로 최소 힙이 만들어지게한 후 n번 비교해서 탐색 -> 시간초과
# heap을 사용하는 이유는 i번 선물을 1번부터 i-1번 선물들이 배정된 이후에 사용 시간이 가장 적은 공정라인에 배정되기 때문에 최소 힙을 사용
# 최소 힙으로 만들면 첫 번째 요소가 제일 작은 값이 되게 때문
# n번 비교하는 것을 heap과 이분탐색 알고리즘을 사용하여 탐색

import sys
input = sys.stdin.readline

import heapq

n, x = map(int, input().split())
present = list(map(int, input().split()))

result = 0
start, end = 1, n # 이분탐색을 위해 start, end 설정, end가 n인 이유는 최대 공정라인의 개수는 n과 같기 때문
while start <= end: # 이분 탐색이 끝날때까지 반복
  mid = (start + end) // 2

  line = [0] * mid # mid만큼 리스트 동적으로 생성, 이유는 공정라인의 최소개수를 찾아야 하므로 mid가 리스트의 길이가 됨
  heapq.heapify(line) # 최소 힙을 만들기 위해서 line을 heap으로 변환
  for i in range(n): # n번 반복
    # line은 최소 힙이므로 첫 번째 요소가 제일 작은 값이 됨
    # 따라서 line의 첫 번째 요소를 heappop후 present의 i번째 요소를 합한 값을 heappush함으로써 present의 모든 요소가 line에 알맞게 배정됨 
    heapq.heappush(line, heapq.heappop(line) + present[i])

  if max(line) <= x: # line의 최대값이 x 이하라면
    result = mid # result에 mid 값 저장, 이때 break 하지 않는 이유는 공정라인의 개수가 최소가 되어야 하므로 공정라인의 개수 최소가 될 수 있는지 계속 탐색 
    end = mid - 1 # 현재 mid 값일 때 line의 최대값이 x이하이므로 end 값을 조정하여 mid의 값보다 작은 값이 있는지 확인
  else: # line의 최대값이 x보다 크다면
    start = mid + 1 # start 값을 조정하여 line의 최대값이 x이하가 될때까지 탐색

print(result)

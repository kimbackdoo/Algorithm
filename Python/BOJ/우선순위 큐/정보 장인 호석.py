# 여러번 틀리고, 시간초과...
# 이름별로 가지고 있는 정보 리스트 생성 -> defaultdict 사용
# 정보는 가장 비싼 가치부터 팔기 때문에 최대 힙 사용

import sys
input = sys.stdin.readline

from collections import defaultdict
import heapq

q = int(input())

info = defaultdict(list) # 고릴라 이름별로 저장하기 위해 defaultdict 생성
result = 0
for _ in range(q):
  query = input().rstrip().split(" ")
  
  if query[0] == "1": # query[0]이 1이라면 정보를 추가하는 쿼리
    for num in list(map(int, query[3:])): # 주어진 k개의 정보를 info[query[1]]에 저장, 이때 num에 음수 값을 주어 최대 힙 생성
      heapq.heappush(info[query[1]], -num)
  else: # query[0]이 2라면 정보를 사는 쿼리
    n = int(query[2])
    while info[query[1]] and n: # info[query[1]]가 비어있지 않고 n이 0이 아니라면 반복
      result += -heapq.heappop(info[query[1]]) # 최대힙에서 제일 큰 값 pop, 이때 값은 음수이므로 다시 양수로 변환 후 result에 더함
      n -= 1 # n개 정보를 사는 것이므로 하나의 정보를 pop할 때마다 n -= 1

print(result)

# 주어진 k개의 배열에서 6개를 뽑아 만들 수 있는 모든 조합을 구하면 됨
# combinations 모듈 이용, 모듈을 사용하지 않는 백트래킹 알고리즘 공부 필요..

import sys
input = sys.stdin.readline

from itertools import combinations

while True:
  nums = input().split()

  if nums[-1] == "0":
    break

  for c in list(combinations(nums[1:], 6)): # 리스트에서 6개를 뽑아 만들 수 있는 모든 조합 구함
    print(*c) # 각각의 조합 출력, Asterisk(*)는 컨테이너 타입(c)를 언팩킹하겠다는 뜻, 즉, (1, 2, 3, 4, 5)를 언팩킹하여 1 2 3 4 5로 변환해줌
  
  print()

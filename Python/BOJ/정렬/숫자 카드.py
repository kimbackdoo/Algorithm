# in을 사용하면 배열의 길이만큼 순회하므로 시간복잡도가 그만큼 높아짐
# list를 사용하는 것보다 set을 사용하여 비교하는 것이 훨씬 빠름

import sys

n = int(sys.stdin.readline().strip())
numbers = set(map(int,sys.stdin.readline().split())) # 비교할 대상 리스트를 set으로 선언

m = int(sys.stdin.readline().strip())
cards = list(map(int,sys.stdin.readline().split()))

for card in cards:
  if card in numbers: # 포함되어 있으면 1, 아니면 0 출력
    print(1, end=" ")
  else:
    print(0, end=" ")

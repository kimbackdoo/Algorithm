# 문제 조건에 맞게 구현하면됨
# R 일때마다 리스트를 뒤집게 되면 시간초과남, 따라서 리스트를 뒤집는 것이 아닌 방향을 바꾸어 pop, popleft 연산 선택하게함
# numbers가 빈문자열이어도 명령이 R이라면 error이 아닌 []가 출력되어야함

import sys
input = sys.stdin.readline

from collections import deque # popleft 연산을 위해 deque 모듈 사용

t = int(input())
for _ in range(t):
  p = input().rstrip() # 명령어 입력, 문자열이기 때문에 rstrip을 이용하여 오른쪽 공백 제거
  n = int(input())
  numbers = input().rstrip() # numbers 입력, 문자열이기 때문에 rstrip을 이용하여 오른쪽 공백 제거

  if n == 0: # n이 0이라면 numbers는 빈문자열
    numbers = []
  else: # n이 0이 아니라면
    numbers = deque(numbers[1:-1].split(",")) # numbers에서 "[", "]" 제거하고 ","를 기준으로 split후 deque로 변환
  
  d, check = 0, True # d: 방향, check: error 판별하기 위함
  for cmd in p: # p의 모든 요소 순회
    if cmd == "R": # R 명령이면
      d = 1 if d == 0 else 0 # 방향 바꿈, 방향 바꾸는 것을 d가 1이면 0, d가 0이면 1로 변환
      
    elif cmd == "D": # D 명령이면
      if not len(numbers): # numbers가 빈 리스트면
        print("error") # error 출력
        check = False # check False로 변환
        break
      
      else: # 요소를 삭제할 수 있으면
        numbers.popleft() if d == 0 else numbers.pop() # d가 0이면 즉, 뒤집히지 않았으면 popleft, 뒤집혔으면 pop 연산 진행
  
  if check: # error가 아니면
    if d == 1: # 방향이 뒤집혔으면
      numbers = list(numbers)[::-1] # numbers 뒤집기
    
    print("[" + ",".join(numbers) + "]") # 출력 형식에 맞게 출력

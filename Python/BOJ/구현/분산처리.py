# ** 연산을 사용하면 시간초과
# a의 제곱수에 따라 일의 자리만 확인하면 됨
# 즉 a가 제곱될 때 일의 자리만 확인하게 되면 1이면 1, ..., a가 2이면 2, 4, 8, 6, ..., a가 3이면 3, 9, 7, 1, ... 으로 됨
# 여기서 반복되는 일의 자리 숫자 리스트를 만들고 b % 리스트의 개수 - 1 요소를 출력하면 정답

t = int(input())
for _ in range(t):
  a, b = map(int, input().split())
  iter = [] # 반복되는 일의 자리 숫자를 위한 리스트
  i = 1
  while True:
    div = a**i % 10 # 일의 자리만 구함
    if div in iter: # 반복되면 break
      break
    
    iter.append(div) # 반복되지 않으면 일의 자리 숫자 append
    i += 1

  idx = b % len(iter) - 1 # 구하고자 하는 인덱스
  print(10) if iter[idx] == 0 else print(iter[idx]) # 일의 자리가 0인 경우는 10이므로 해당 인덱스의 요소가 0일 경우 10, 아니면 해당 요소 출력

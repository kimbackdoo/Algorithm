# 동전의 단위가 25, 10, 5, 1이므로 가장 큰 단위부터 계산하면 최소 동전 개수가 나옴, 그리디 알고리즘 적용

money = [25, 10, 5, 1] # 동전의 단위 리스트

t = int(input())
for _ in range(t):
  c = int(input())
  result = []
  for coin in money:
    result.append(c // coin) # 거스름돈을 각 동전의 단위로 나누었을 때 몫을 result에 저장
    c %= coin # 거스름돈을 각 동전의 단위로 나누었을 때 나머지로 만들면서 반복
  
  print(" ".join(map(str, result)))

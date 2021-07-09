# 별의 개수가 1, 3, 5, 7, ... 2n-1로 증가
# 별의 개수에 따라 공백이 n-1, n-2, ... 0으로 감소

n = int(input())
for i in range(n-1, -1, -1): # 역순 for문
  # 공백의 개수를 n-1, n-2, ... 0으로 감소하고
  # 별의 개수를 1, 3, 5, ... 2n-1 증가시킴
  # 2n-1-2i에서 2i인 이유는 별을 기준으로 양쪽 대칭이기 때문
  s = " " * i + "*" * (2*n-1-2*i)
  print(s)

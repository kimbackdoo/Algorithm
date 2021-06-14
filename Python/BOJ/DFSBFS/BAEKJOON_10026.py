# R, G, B를 구분하는 리스트와 (R, G), B를 구분하는 리스트 2개를 생성
# R=0, G=1, B=2, R=0, G=0, B=1로 두고 각각 matrix1, matrix2에 저장
# bfs를 정의하여 매개변수로 들어온 리스트 탐색
# 즉, 일반 사람과 적록색약인 사람의 경우를 각각 나누어 탐색

from collections import deque

def bfs(x, y, num, matrix): # bfs 정의
  queue = deque()
  queue.append((x, y))
  while queue:
    x, y = queue.popleft()
    for i in range(4):
      nx, ny = x + move[i][0], y + move[i][1]
      if 0 <= nx < n and 0 <= ny < n and matrix[nx][ny] == num:
        matrix[nx][ny] = 101
        queue.append((nx, ny))

n = int(input())

matrix1, matrix2 = [], [] # 일반 사람과 적록색약인 사람 정보를 담을 리스트
for _ in range(n):
  colors = input()
  tmp1, tmp2 = [], []
  for color in colors: # 일반 사람과 적록색약인 사람 각각을 저장
    if color == "R":
      tmp1.append(0)
      tmp2.append(0)
    elif color == "G":
      tmp1.append(1)
      tmp2.append(0)
    elif color == "B":
      tmp1.append(2)
      tmp2.append(1)
  
  matrix1.append(tmp1)
  matrix2.append(tmp2)
  
move = [(1, 0), (-1, 0), (0, 1), (0, -1)]

result1, result2 = 0, 0
for i in range(n):
  for j in range(n):
    for k in range(3): # R=0, G=1, B=2 이므로 0 ~ 2까지 반복하면서 일반 사람과 적록색약인 사람 각각 탐색
      if matrix1[i][j] == k:
        bfs(i, j, k, matrix1)
        result1 += 1
      if matrix2[i][j] == k:
        bfs(i, j, k, matrix2)
        result2 += 1

print(result1, result2)

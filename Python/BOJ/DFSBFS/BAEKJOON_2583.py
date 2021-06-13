from collections import deque

def bfs(x, y): # bfs 정의
  queue = deque()
  queue.append((x, y))
  matrix[x][y] = 1
  cnt = 1 # 사각형의 면적 == 사각형의 개수
  while queue:
    x, y = queue.popleft()
    for i in range(4):
      nx, ny = x + move[i][0], y + move[i][1] # 다음 노드
      if 0 <= nx < m and 0 <= ny < n and matrix[nx][ny] == 0: # 좌표가 조건 안에 있고 다음 노드가 0일 경우
        queue.append((nx, ny))
        matrix[nx][ny] = 1
        cnt += 1 # 사각형 개수 count

  return cnt

m, n, k = map(int, input().split())

matrix = [[0] * n for _ in range(m)]
for _ in range(k):
  y, x, y1, x1 = map(int, input().split())

  for i in range(x, x1): # 리스트에서 입력 받은 좌표 값을 1로 저장
    for j in range(y, y1):
      matrix[i][j] = 1

move = [(1, 0), (-1, 0), (0, 1), (0, -1)] # 노드는 상하좌우 움직일 수 있음

result = 0
answer = []
for i in range(m): # 노드가 0인 것을 찾아 bfs 탐색
  for j in range(n):
    if matrix[i][j] == 0:
      answer.append(bfs(i, j))
      result += 1 # bfs 한번 끝날 때마다 count

print(result)
for a in sorted(answer): # 오름차순 정렬
  print(a, end=" ")

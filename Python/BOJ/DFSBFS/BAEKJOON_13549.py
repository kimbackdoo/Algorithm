from collections import deque

n, k = map(int, input().split())

MAX = 10**5 + 1
matrix = [0] * MAX

dx = [-1, 1, 2]

def bfs(x):
  queue = deque()
  queue.append(x)
  matrix[x] = 1
  while queue:
    x = queue.popleft()
    if x == k:
      print(matrix[k] - 1)
      return
    for nx in (x-1, x+1, x*2):
      if 0 <= nx < MAX and matrix[nx] == 0:
        if nx == x*2 and x != 0:
          matrix[nx] = matrix[x]
          queue.appendleft(nx)
        else:
          matrix[nx] = matrix[x] + 1
          queue.append(nx)

  print(matrix[k] - 1)
  
bfs(n)

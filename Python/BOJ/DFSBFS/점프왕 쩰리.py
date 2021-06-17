# (0, 0)에서 (n-1, n-1)까지 도달할 수 있는지 확인하는 것이므로 BFS 탐색 알고리즘 적용
# 오른쪽, 아래쪽로만 움직일 수 있고, 현재 밟고 있는 칸에 쓰여진 숫자 만큼 이동 가능
# 따라서 오른쪽, 아래쪽으로 움직이면서 현재 밟고 있는 칸에 쓰여진 숫자 만큼 이동하면서 탐색

from collections import deque

def bfs(x, y): # BFS 구현
  queue = deque()
  queue.append((x, y))
  visited[x][y] = 1 # 방문 처리
  while queue:
    x, y = queue.popleft()
    for i in range(2):
      # 오른쪽, 아래쪽으로 움직이면서 현재 밟고 있는 칸에 쓰여진 숫자만큼 이동하므로 * 사용하면 다음 이동 좌표를 구할 수 있음
      nx, ny = x + move[i][0]*maps[x][y], y + move[i][1]*maps[x][y]
      if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == 0: # 다음 좌표가 범위 안에 있고 방문하지 않았으면
        if (nx, ny) == (n-1, n-1): # 전부다 탐색하지 않고 중간에 (n-1, n-1) 좌표에 도달할 수 있으면 return, 속도 개선
          return "HaruHaru"

        queue.append((nx, ny))
        visited[nx][ny] = 1 # 방문 처리

  return "Hing" # 모두 탐색 하였는데 (n-1, n-1)에 도달하지 못했으면 return

n = int(input())

maps = []
for _ in range(n):
  maps.append(list(map(int, input().split())))

move = [(0, 1), (1, 0)] # 오른쪽, 아래쪽으로만 움직일 수 있음
visited = [[0] * n for _ in range(n)] # 방문 체크를 위한 리스트

print(bfs(0, 0))

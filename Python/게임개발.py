# 다시 풀 것
n, m = map(int, input().split())
x, y, d = map(int, input().split())
gameMap = []
for _ in range(n):
  gameMap.append(list(map(int, input().split())))

check = [[0]*m for _ in range(n)]
check[x][y] = 1

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def turn_left():
  global d
  d -= 1
  if d == -1:
    d=3

cnt = 1
turn_chk = 0
while True:
  turn_left()
  nx = x + dx[d]
  ny = y + dy[d]

  if check[nx][ny]==0 and gameMap[nx][ny]==0:
    check[nx][ny]=1
    x = nx
    y = ny
    cnt += 1
    turn_chk = 0
    continue
  else:
    turn_chk += 1

  if turn_chk == 4:
    nx = x - dx[d]
    ny = y - dx[d]

    if gameMap[nx][ny]==1:
      x = nx
      y = ny
    else:
      break
    
    turn_time = 0

print(cnt)
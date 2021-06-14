# bfs로 maps를 탐색 후 상대 진영팀까지의 거리를 구함
# 그 전 지점까지의 거리 + 1을 하게 되면 최단거리가 계산됨

from collections import deque

def bfs(x, y, maps): # bfs 구현
    move = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    
    queue = deque()
    queue.append((x, y))
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x + move[i][0], y + move[i][1]
            if 0 <= nx < len(maps) and 0 <= ny < len(maps[0]) and maps[nx][ny] == 1: # nx, ny가 게임 맵 안에 있고 다음 움직일 곳이 벽이 아니면 즉 1이면
                maps[nx][ny] = maps[x][y] + 1 # 그 전 지점에서 + 1
                queue.append((nx, ny))
                
    return maps[len(maps)-1][len(maps[0])-1]

def solution(maps):
    answer = bfs(0, 0, maps)
    return answer if answer != 1 else -1

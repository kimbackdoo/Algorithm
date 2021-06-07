from collections import deque

def bfs(x, y, maps):
    queue = deque()
    queue.append((x,y))

    dx = [-1, 1, 0, 0] # 좌, 우
    dy = [0, 0, -1, 1] # 상, 하

    while queue: # 큐가 빌 때까지
        x, y = queue.popleft()
        for i in range(4): # 상, 하, 좌, 우 움직이면서 확인
            nx, ny = x + dx[i], y + dy[i]
            # nx, ny가 범위 안에 있으면서 다음 이동 장소가 1일 경우만
            if 0 <= nx < len(maps) and 0 <= ny < len(maps[0]) and maps[nx][ny] == 1:
                maps[nx][ny] = maps[x][y] + 1 # 그 전 위치 값에 +1씩 더해나가면서 최단 거리 계산
                queue.append((nx, ny))

    return maps[len(maps) - 1][len(maps[0]) - 1] # 상대 팀 진영까지 최단 거리 반환

def solution(maps):
    answer = bfs(0, 0, maps)

    if answer == 1: return -1
    else: return answer

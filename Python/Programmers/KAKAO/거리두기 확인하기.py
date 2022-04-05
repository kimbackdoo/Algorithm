# 문제 조건에 따라 거리두기가 되고 있는지 아닌지 확인하면됨
# P 위치에서 상, 하, 좌, 우로 탐색하면서 거리두기가 지켜지고 있는지 확인
# 이때, 처음 P 위치에서 거리가 2이하이고, X일때는 탐색하지 못하므로, bfs 알고리즘을 이용하여 조건에 맞게 탐색

from collections import deque

def distance_check(x1, y1, x2, y2): # 맨해튼 거리가 2이하이어야 하므로, 맨해튼 거리가 2이하인지 확인하는 함수
    return (abs(x1 - x2) + abs(y1 - y2)) <= 2

def bfs(place, x, y, visited, move): # bfs 알고리즘 구현
    queue = deque()
    queue.append((x, y))
    visited[x][y] = True # (x, y)번째 요소 방문처리
    curX, curY = x, y # 거리를 계산하기 위해 초기 x, y 값 저장
    while queue:
        x, y = queue.popleft()
        for i in range(4): # 상, 하, 좌, 우로 움직인
            nx, ny = x + move[i][0], y + move[i][1]
            if 0 <= nx < 5 and 0 <= ny < 5 and not visited[nx][ny]: # 다음 위치가 범위 안에 있고, 방문하지 않았으면
                if distance_check(curX, curY, nx, ny) and place[nx][ny] != "X": # 맨해튼 거리가 2 이하이고, X가 아니라면
                    queue.append((nx, ny)) # queue에 append
                    visited[nx][ny] = True # 방문 처리
                    if place[nx][ny] == "P": # 거리두기가 지켜지고 있지 않으면
                        return False # 더 탐색하지 않고 False return
    
    return True # 거리두기가 지켜지고 있으면 True return

def check(place, visited, move): # 거리두기가 지켜지고 있는지, 아닌지 확인하는 함수
    for x in range(5):
        for y in range(5):
            if place[x][y] == "P" and not visited[x][y]: # (x, y)번째 요소가 P이고 아직 방문하지 않았으면
                if not bfs(place, x, y, visited, move): # bfs 탐색 후 거리두기가 지켜지고 있지 않으면
                    return False # 더 탐색하지 않고, False return
    
    return True # 거리두기가 지켜지고 있으면 True return

def solution(places):
    answer = []
    move = [(1, 0), (-1, 0), (0, 1), (0, -1)] # 상, 하, 좌, 우로 움직이기 위한 리스트
    for place in places: # places의 모든 요소 순회
        visited = [[False] * 5 for _ in range(5)] # 방문처리할 visited 리스트
        answer.append(1 if check(place, visited, move) else 0) # 거리두기가 지켜지고 있으면 1, 지켜지고 있지 않으면 0 append
            
    return answer

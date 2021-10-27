# 각 격자에서 빛은 상, 하, 좌, 우 방향으로 쏠 수 있음
# 모든 경우를 확인하면 시간초과가 나므로 경로를 미리 저장하여 방문하지 않은 경로만 탐색
# 예를 들어, x행 y열에서 (0, 1) 방향으로 빛을 쐈다면 visited[x][y][0] = True로 만듦으로써 방문여부 확인

def solution(grid):
    move = [(0, 1), (1, 0), (0, -1), (-1, 0)] # 빛은 상, 하, 좌, 우로 쏠 수 있고, "L"일때는 리스트의 왼쪽, "R"일때는 리스트의 오른쪽이 된다.
    route = {}
    visited = [[[False] * 4 for _ in range(len(grid[0]))] for _ in range(len(grid))] # 방문여부를 확인할 3차원 리스트, 행, 열, 빛의 방향을 모두 저장해야 하므로 3차원 리스트로 선언
    for i in range(len(grid)): # 행 순회
        for j in range(len(grid[0])): # 열 순회
            for k in range(4): # move 모든 요소 순회
                x, y = i, j # i, j 값 기억
                cnt, idx = 0, k # 사이클 counting할 cnt, 빛을 쐈을때 순환하는 것을 표현하기 위해 idx로 move 리스트를 순회한다.
                tmp = []
                if not visited[x][y][idx]: # x행, y열의 idx번째 방향으로 빛을 쏘지 않았다면
                    while True:
                        visited[x][y][idx] = True # 방문 처리
                        if grid[x][y] == "L": idx = (idx - 1) % 4 # "L"일 경우 idx의 왼쪽 방향으로 빛이 꺾임
                        elif grid[x][y] == "R": idx = (idx + 1) % 4 # "R"일 경우 idx의 오른쪽 방향으로 빛이 꺾임
                        
                        # x, y에 다음 위치를 저장
                        x += move[idx][0]
                        y += move[idx][1]
                        tmp.append((x, y)) # 빛이 이동할때 모든 좌표 tmp에 append
                        x, y = (x % len(grid)), (y % len(grid[0])) # x, y가 격자 범위를 벗어날 수 있으므로 벗어났을 경우 반대편으로 돌아오기 때문에 % 연산자 이용
                        cnt += 1 # 사이클 counting

                        if x == i and y == j and idx == k: # 빛을 쏘고 처음으로 돌아왔다면
                            break # break

                    if tuple(sorted(tmp)) not in route: # route에 해당 경로가 없으면
                        route[tuple(sorted(tmp))] = cnt # 해당경로를 key, value를 cnt로 설정
    
    return sorted(route.values()) # route의 모든 value 값을 가져오고 오름차순 정렬 후 return

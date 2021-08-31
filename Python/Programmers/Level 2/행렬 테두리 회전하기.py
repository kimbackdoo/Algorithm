# 문제를 이해하면 생각보다 어렵지 않게 구현할 수 있음
# 문제 조건에 따라 행렬을 회전시키면 됨
# 시계방향으로 회전을 하므로 우, 하, 좌, 상 방향으로 움직임, 이것을 이용하여 행렬 회전

def solution(rows, columns, queries):
    matrix = [[i * columns + (j + 1) for j in range(columns)] for i in range(rows)] # 2차원 리스트 matrix에 초기 값 설정
    move = [(0, 1), (1, 0), (0, -1), (-1, 0)] # 행렬은 우, 하, 좌, 상 즉, 시계방향으로 움직임
    answer = []
    for x1, y1, x2, y2 in queries: # queries의 모든 요소 순회
        x, y = x1 - 1, y1 - 1 # x, y에 행렬 회전의 시작점 저장
        idx = 0 # move 리스트의 인덱스를 뜻하는 변수
        rotate = [matrix[x1 - 1][y1 - 1]] # 회전할 때 회전할 요소의 값을 저장
        while True:
            nx, ny = x + move[idx][0], y + move[idx][1] # nx, ny에 다음 이동할 위치를 저장 
            if nx < (x1 - 1) or nx >= x2 or ny < (y1 - 1) or ny >= y2: # nx, ny가 행렬 테두리의 범위를 벗어난다면 방향이 바뀐다는 뜻
                idx += 1 # idx의 값을 증가시켜 방향을 바꿈
                nx, ny = x + move[idx][0], y + move[idx][1] # nx, ny에 다음 위치 저장

            tmp = matrix[nx][ny] # tmp에 matrix[nx][ny] 값 저장
            matrix[nx][ny] = rotate[-1] # matrix[nx][ny]에 rotate의 마지막 요소 저장
            x, y = nx, ny # x, y 값 갱신
            if x == (x1 - 1) and y == (y1 - 1): # x, y가 시작점이라면 즉, 한바퀴 회전을 하였으면 break
                break
            
            rotate.append(tmp) # rotate에 tmp값 append
        
        answer.append(min(rotate)) # rotate에서 제일 작은 값 answer에 append
        
    return answer

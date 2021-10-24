# 주어진 조건대로 숫자를 나열하면됨
# 반시계 방향으로 숫자가 증가하므로, (1, 0), (0, 1), (-1, -1) 방향으로 좌표값이 증가함
# n = 5라면, [0], [0, 0], [0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0, 0]으로 리스트를 만들고 숫자를 채워넣음

# def solution(n):
#     numbers = [[0] * i for i in range(1, n + 1)] # 초기 리스트 설정
#     numbers[0][0] = 1 # (0, 0)번째 요소는 항상 1이므로 1로 변경
#     x, y, idx = 0, 0, 0
#     total = n * (n + 1) // 2 # n의 최대값을 1부터 n까지의 합이므로 공식을 사용하여 1부터 n까지의 합을 구함
#     move = [(1, 0), (0, 1), (-1, -1)] # 반시계 방향으로 회전시키기 위한 리스트
#     while numbers[x][y] != total: # numbers[x][y]가 total이면 모든 리스트에 숫자를 채운 것이므로 stop
#         nx, ny = x + move[idx % 3][0], y + move[idx % 3][1] # 현재 방향에 맞게 nx, ny 값 설정
#         if 0 <= nx < n and 0 <= ny < len(numbers[nx]) and not numbers[nx][ny]: # nx와 ny가 numbers 범위 안에 있고, numbers[nx][ny]에 아직 방문하지 않았다면
#             numbers[nx][ny] = numbers[x][y] + 1 # numbers[nx][ny]는 numbers[x][y] + 1이므로 numbers[nx][ny]값 설정
#             x, y = nx, ny # x, y값 nx, ny 값으로 변경
#         else: # nx, ny과 범위를 벗어났거나, 방문하였다면
#             idx += 1 # 방향 바꿈
    
#     answer = []
#     for num in numbers:
#         answer += num # answer에 numbers의 모든 요소 1차원 리스트로 변환
    
#     return answer

def solution(n):
    numbers = [[0] * i for i in range(1, n + 1)]
    numbers[0][0] = 1
    x, y, idx = 0, 0, 0
    total = n * (n + 1) // 2
    move = [(1, 0), (0, 1), (-1, -1)]
    while numbers[x][y] != total:
        nx, ny = x + move[idx % 3][0], y + move[idx % 3][1]
        if 0 <= nx < n and 0 <= ny < len(numbers[nx]) and not numbers[nx][ny]:
            numbers[nx][ny] = numbers[x][y] + 1
            x, y = nx, ny
        else:
            idx += 1
    
    # sum 함수를 이용하여 리스트를 합칠 수 있음, 속도는 for문에 비해 느림
    # sum 함수의 두번째 인자는 default 값으로 0, 리스트를 합치기 위해서는 두번째 인자로 []을 넣어야함
    return sum(numbers, [])

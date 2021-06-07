from collections import deque

def solution(n, computers):
    answer = 0

    visited = [0] * n # 방문을 확인하기 위해 크기가 n 리스트 선언
    queue = deque()
    while 0 in visited: # 모든 컴퓨터가 연결되어 있지 않으므로 모든 컴퓨터가 방문 되도록 반복
        queue.append(visited.index(0)) # 처음 0의 위치
        while queue:
            v = queue.popleft()
            for i in range(n):
                if visited[i] == 0 and computers[v][i] == 1: # 아직 방문하지 않았고 컴퓨터 값이 1이라면
                    queue.append(i)
                    visited[i] = 1
        answer += 1 # 연결된 컴퓨터가 없으면 +1

    return answer

# 현재 행에서 열이 같지 않으면서 전 행의 최대값을 더해나가고 마지막 행에서 최대값이 최고점이 된다. 즉, DP 문제
# f(i, 0) = max(f(i-1, 1), f(i-1, 2), f(i-1, 3))

def solution(land):
    for i in range(1, len(land)): # land의 열 수는 4로 고정
        # 현재 열과 이전 행의 열이 겹치지 않으면서 각 열의 점수와 이전 행의 최대값을 더해나감
        land[i][0] += max(land[i-1][1], land[i-1][2], land[i-1][3])
        land[i][1] += max(land[i-1][0], land[i-1][2], land[i-1][3])
        land[i][2] += max(land[i-1][0], land[i-1][1], land[i-1][3])
        land[i][3] += max(land[i-1][0], land[i-1][1], land[i-1][2])
        
    return max(land[len(land)-1]) # 마지막 행에서 최대값이 최고점

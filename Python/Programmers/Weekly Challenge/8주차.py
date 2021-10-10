# 가로, 세로를 적절하게 돌려 모든 명함을 수납할 수 있는 가장 작은 지갑을 만들면 됨
# 즉, sizes의 모든 요소를 순회하면서 가로에는 가로, 세로 중 큰 값을, 세로에는 가로, 세로 중 작은 값을 저장
# 변환한 가로, 세로 리스트 중에서 제일 큰 값을 곱하면 정답이 됨

# def solution(sizes):
#     row, col = [], [] # 변환한 가로, 세로의 값들을 저장할 리스트
#     for r, c in sizes: # sizes의 모든 요소 순회
#         if r < c: # 세로의 값이 더 크다면
#             r, c = c, r # swap
        
#         row.append(r) # 가로 리스트에 가로 값들 저장
#         col.append(c) # 세로 리스트에 세로 값들 저장
        
#     return max(row) * max(col) # 가로, 세로 리스트 중에서 제일 큰 값 곱하기

# def solution(sizes):
#     row, col = [], []
#     for r, c in sizes:
#         # if문을 사용하지 않고 리스트에 바로 append
#         row.append(max(r, c))
#         col.append(min(r, c))
        
#     return max(row) * max(col)

def solution(sizes):
    # 리스트 컴프리헨션을 이용하여 가로, 세로의 값을 구함
    return max(max(x) for x in sizes) * max(min(y) for y in sizes)

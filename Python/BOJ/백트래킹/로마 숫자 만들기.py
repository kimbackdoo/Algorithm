# 1, 5, 10, 50 중에서 N개를 뽑아 만들 수 있는 모든 경우를 세면 됨
# 합이 중복되면 안됨, 즉, dfs 알고리즘을 이용하여 중복 조합 구현
# 1, 5의 합과 5, 1의 합은 같으므로 현재 인덱스 이후의 값들만 탐색하면 됨

# n = int(input())

# numbers = [1, 5, 10, 50]
# result = set() # 결과는 중복되면 안되므로 집합 사용
# def dfs(idx, combi): # dfs 구현
#   if len(combi) == n: # combi의 길이가 n과 같다면 즉, n개를 뽑았다면
#     result.add(sum(combi)) # result에 combi의 합 add
#     return # 재귀 탈출

#   for i in range(idx, 4): # numbers의 모든 요소 순회
#     dfs(i, combi + [numbers[i]]) # dfs 탐색, 현재 인덱스부터 탐색하면 됨

# dfs(0, [])
# print(len(result))

# 내장함수 sum을 사용하지 않고 dfs 탐색하면서 바로 합을 계산하여 result에 추가

n = int(input())

roma = [1, 5, 10, 50]
result = set()
def dfs(total, depth, idx):
  if depth == n: # depth가 n과 같다면, 즉, n개를 뽑았다면
    result.add(total)
    return
  
  for i in range(idx, 4):
    dfs(total + roma[i], depth + 1, i) # dfs 탐색, 첫번째 인자에 합한 결과, 두번째 인자에 depth + 1, 3번째 인자에 현재 인덱스 값을 넣어 탐색

dfs(0, 0, 0)
print(len(result))

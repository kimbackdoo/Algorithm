# 입력 받은 수열 중에서 몇 개의 수를 뽑았을 때, 합이 s가 되는 경우의 수를 구하면됨, 즉, 조합을 구하면 됨
# dfs 탐색을 이용하여 입력 받은 수열 중에서 합이 s가 되는 경우를 모두 구함

# import sys
# input = sys.stdin.readline

# def dfs(idx, total): # dfs 알고리즘 구현
#   global cnt

#   if total == s: # total이 s가 되면 count
#     cnt += 1

#   # numbers의 모든 요소를 순회하면서 dfs 탐색
#   # 이때, 조합을 구하는 것이므로 한번 뽑았던 경우는 다시 뽑지 않기 위해서 idx 값을 i + 1로 설정, 이유는 i번째 이전의 요소는 이미 뽑았기 때문에 i번째 이후의 요소만 생각
#   for i in range(idx, n):
#     dfs(i + 1, total + numbers[i])

# n, s = map(int, input().split())
# numbers = list(map(int, input().split()))

# cnt = 0
# dfs(0, 0) # dfs 탐색
# print(cnt - 1 if s == 0 else cnt) # dfs 탐색을 할 때 초기값으로 0을 넣었기 때문에 s가 0이라면 모든 경우 + 1이 되므로 s가 0일 경우 -1을 해줌

# 수열의 모든 요소를 탐색할 때, 해당 요소를 뽑는 경우와 안뽑는 경우로 나누어서 생각할 수 있음
# 따라서 for문을 사용하지 않고 dfs 탐색 가능

import sys
input = sys.stdin.readline

def dfs(idx, total):
  global cnt

  if idx == n: # idx가 numbers의 길이가 된다면 return, 즉, 재귀 탈출
    return

  if total + numbers[idx] == s: # TODO total == s가 아니라 total + numbers[idx] == s 인 이유 다시 확인할 것
    cnt += 1

  dfs(idx + 1, total) # idx번째 요소를 뽑지 않는 경우
  dfs(idx + 1, total + numbers[idx]) # idx번째 요소를 뽑는 경우

n, s = map(int, input().split())
numbers = list(map(int, input().split()))

cnt = 0
dfs(0, 0)
print(cnt)

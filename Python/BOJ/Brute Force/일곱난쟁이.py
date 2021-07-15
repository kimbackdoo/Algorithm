# 입력받은 9개의 요소들 중에서 7개를 선택했을 때 합이 100이 되는 경우를 출력하면 됨

# from itertools import combinations

# height = [int(input()) for _ in range(9)] # 리스트 컴프리헨션을 이용하여 난쟁이 키 입력 받음

# for combi in list(combinations(height, 7)): # 9개의 요소 중에서 7개를 고르는 모든 경우를 순회
#   if sum(combi) == 100: # 합이 100이 되는 것이 있다면
#     for c in sorted(combi): # 오름차순 정렬 후 출력
#       print(c)

#     break # 합이 100이 되는 경우 하나만 출력하면 되므로 모든 경우를 순회하지 않고 break

# height의 합에서 2개 요소를 제거했을 때 합이 100이 되는 경우를 생각하면 됨
height = [int(input()) for _ in range(9)]

height.sort()
total = sum(height)
for i in range(9):
  for j in range(i+1, 9):
    if (total - height[i] - height[j]) == 100: # 전체 합에서 2개 요소를 제거했을 때 100이 되는 경우를 찾음
      for k in range(9): # k가 i, j가 아닌 모든 요소를 출력
        if k != i and k != j:
          print(k)
      
      exit() # 프로그램 종료

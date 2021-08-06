# A, B, BA, BAB, BABBA -> (1, 0), (0, 1), (1, 1), (1, 2), (2, 3), ...
# 즉, k번 눌렀을 때 A, B의 개수는 (a(k-1) + a(k-2), b(k-1) + b(k-2))가 됨
# 처음에 dp = [[0, 0]] * (k+1)로 2차원 리스트를 생성하였으나, 이렇게 하면 리스트 복사가 되어 참조값이 모두 같게 되므로 i번째 요소를 바꿀 때 다른 요소의 값들도 바뀌게 됨
# a, b리스트를 각각 만들어 append 하는 방식으로 수정

k = int(input())

a = [1, 0] # A의 개수를 저장할 리스트
b = [0, 1] # B의 개수를 저장할 리스트
for i in range(2, k+1):
  # 위 점화식에 맞게 a, b 리스트 각각 append
  a.append(a[i-1] + a[i-2])
  b.append(b[i-1] + b[i-2])

print(a[k], b[k])
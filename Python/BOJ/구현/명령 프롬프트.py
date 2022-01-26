# 문제 조건에 맞게 구현하면됨
# 입력받은 문자열 중에서 서로 다른 글자를 찾으면 됨
# 서로 다른 글자를 찾기 위해 중첩 for문을 사용하여 모든 경우를 확인, bruteforce
import sys
input = sys.stdin.readline

n = int(input())
files = [input().strip() for _ in range(n)]

answer = list(files[0]) # answer에 files의 첫번째 요소를 리스트로 변환하여 저장
for i in range(1, n): # 1부터 n - 1까지 모든 요소 순회
  for j in range(len(answer)): # 글자를 비교하기 위해 files의 요소의 길이만큼 순회
    # answer[j]와 files[i][j]가 다르면 와일드카드 문자(?)를 써야 하므로 answer[j]를 ?로 변환
    # 이때, answer[j]가 이미 ? 라면 answer[j]의 값을 바꿀 필요가 없으므로 answer[j]가 ?가 아닌 경우로 제한
    if answer[j] != files[i][j] and answer[j] != "?":
      answer[j] = "?"

print("".join(answer)) # answer은 리스트이므로 문자열로 변환 후 출력

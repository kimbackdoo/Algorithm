# 조건에 맞게 정렬하면 됨

scores = []
for i in range(8):
  score = int(input())
  scores.append((score, i+1)) # 문제 번호도 출력해야 하므로 (점수, 문제번호) 튜플로 append

result = 0
nums = []
for score in sorted(scores, reverse=True)[:5]: # 역순 정렬 후 5개까지의 점수의 합이 총점수이므로 역순 정렬 후 5번 반복
  result += score[0] # 총점수 계산
  nums.append(score[1]) # 문제 번호 append

print(result)
print(" ".join(map(str, sorted(nums)))) # 오름차순 정렬된 nums의 각 원소를 str로 변환하고 join을 사용하여 문자열로 변환

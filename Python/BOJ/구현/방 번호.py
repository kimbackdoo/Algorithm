# 0 ~ 9 인덱스를 가진 리스트를 생성
# 입력받은 n의 모든 숫자를 count
# 단, 숫자가 6, 9일 경우 서로 뒤집을 수 있기 때문에 리스트에서 둘 중 작은 숫자를 1 증가

n = list(map(int, input()))

cnt = [0] * 10 # 0 ~ 9 인덱스를 가진 리스트
for num in n:
  if num == 6 or num == 9: # 숫자가 6, 9일 경우
    if cnt[6] <= cnt[9]: # 만약 cnt[6]이 작거나 같다면 +1 증가
      cnt[6] += 1
    else: # 아니라면 +1 증가
      cnt[9] += 1
  else: # 6, 9를 제외한 숫자라면 +1 증가
    cnt[num] += 1

print(max(cnt)) # 최대값이 최소 세트의 개수가 됨

# 문제 조건을 그대로 구현하면 됨
# 최빈값을 구할 때 파이썬의 Counter 라이브러리 사용

from collections import Counter

n = int(input())

numbers = []
for _ in range(n):
  numbers.append(int(input()))

print(round(sum(numbers) / n)) # 산술평균 출력

numbers.sort()
print(sorted(numbers)[n//2]) # 중앙값 출력, n이 홀수로 정해져 있으므로 2로 나눈 몫이 중앙값이 됨
# 최빈값을 구하기 위해 Counter 모듈 사용
counter = Counter(numbers).most_common() # most_common()은 최빈값을 기준으로 내림차순 정렬 후 해당 숫자와 빈도수를 튜플로 반환
max = counter[0][1] # 빈도수를 기준으로 내림차순 정렬되어 있으므로 첫번째 값이 최빈값이다.

freq = [] # 최빈값이 담길 리스트
for c in counter: # counter 리스트를 순회
  if c[1] == max: # 순회하면서 최빈값과 같은 수가 있다면
    freq.append(c[0]) # freq 리스트에 저장
# 위에서 numbers를 오름차순 정렬했으므로 최빈값 리스트 freq도 오름차순 정렬되어 있음
print(freq[1] if len(freq) >= 2 else freq[0]) # 최빈값이 2개 이상이라면 두번째로 작은 수 출력, 최빈값이 1개라면 최빈값 출력
print(numbers[-1] - numbers[0]) # numbers가 오름차순 정렬되어 있으므로 마지막 값에서 첫번째 값의 차이를 출력

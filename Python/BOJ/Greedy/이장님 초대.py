# 나무를 심는데 1일이 걸리므로 동시에 여러 나무를 심지는 못한다.
# 즉, 나무가 자라는데 제일 오래걸리는 나무부터 심어야 이장님을 빨리 초대할 수 있다. 따라서 내림차순 정렬
# 나무를 심고 나무가 자라는 총 걸리는 시간의 최대값 + 1이 정답이 됨
# 예를 들어, 2 3 4 3 라면 내림차순 정렬 후 4 3 3 2가 되고, 총 걸리는 시간은 5 5 6 6이 됨
# 따라서 이장님을 초대할 수 있는 날짜는 모든 나무가 다 자란 6일 다음날인 7일날 초대할 수 있음

import sys
input = sys.stdin.readline

n = int(input())
t = sorted(map(int, input().split()), reverse=True) # 입력받으면서 내림차순 정렬

result = max(map(lambda x: x[0] + x[1] + 1, enumerate(t))) # enumerate 함수를 사용하여 index 값을 추출하고 map과 람다식을 이용하여 총 걸리는 시간을 구함, 이후 최대값을 구함
print(result + 1) # 나무가 다 자라고 다음날 초대할 수 있으므로 result + 1 출력

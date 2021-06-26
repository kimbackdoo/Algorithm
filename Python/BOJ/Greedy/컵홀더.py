# 컵홀더의 개수와 좌석 개수 중 작은 것을 출력 

n = int(input())
seats = input()

cnt = 0
for seat in seats:
  if seat == "L": # 커플석의 개수를 구함
    cnt += 1

cup = (n + 1) - (cnt // 2) # 컵홀더의 개수 구함
print(min(n, cup)) # n, cup 중 작은 것을 출력

# 문제에서 요구한대로 구현한 후 모든 경우를 탐색
# 숫자는 0부터 시작할 수도 있는 조건 체크
# 중복순열(product)를 이용하여 led 딕셔너리에서 k개를 뽑아 만들 수 있는 모든 경우의 수에서 x와 비교하여 반전시킬 수 있는지 확인 

# from itertools import product

# led = { # led dict
#   "0": "1111110",
#   "1": "0110000",
#   "2": "1101101",
#   "3": "1111001",
#   "4": "0110011",
#   "5": "1011011",
#   "6": "1011111",
#   "7": "1110000",
#   "8": "1111111",
#   "9": "1111011"
# }

# n, k, p, x = map(int, input().split())

# x = "0" * (k - len(str(x))) + str(x) # 숫자는 0부터 시작할 수 있으므로 x를 문자열로 변환 후 k - len(str(x)) 만큼 앞에 0을 붙임
# current = ""
# for num in x:
#   current += led[num] # current에 x를 led로 변환한 수 저장

# result = 0
# for num in set(map("".join, product(led, repeat=k))): # led에서 k개를 뽑아 만들 수 있는 모든 중복순열의 수 반복
#   if 1 <= int(num) <= n: # 1층부터 N층까지 이용 가능하므로
#     tmp = ""
#     for i in num:
#       tmp += led[i] # tmp에 num을 led로 변환한 수 저장

#     cnt = sum([1 for i in range(len(current)) if current[i] != tmp[i]]) # 반전시킬 수 있는 개수 count
#     if 1 <= cnt <= p: # 최소 1개, 최대 p개 반전 시킬 수 있으므로, 범위에 있으면 count
#       result += 1

# print(result)

# 굳이 product 모듈을 사용하지 않고 1 ~ N까지 경우 탐색하면 됨
led = {
  "0": "1111110",
  "1": "0110000",
  "2": "1101101",
  "3": "1111001",
  "4": "0110011",
  "5": "1011011",
  "6": "1011111",
  "7": "1110000",
  "8": "1111111",
  "9": "1111011"
}

n, k, p, x = map(int, input().split())

current = ""
x = "0" * (k - len(str(x))) + str(x)
for num in x:
  current += led[num]

result = 0
for num in range(1, n+1): # 1 ~ N까지 모든 경우 탐색
  num = "0" * (k - len(str(num))) + str(num) # 숫자는 0부터 시작할 수 있으므로 num을 문자열로 변환 후 k - len(str(x)) 만큼 앞에 0을 붙임
  
  tmp = ""
  for i in num:
    tmp += led[i]

  cnt = sum([1 for i in range(len(current)) if current[i] != tmp[i]])
  if 1 <= cnt <= p:
    result += 1

print(result)

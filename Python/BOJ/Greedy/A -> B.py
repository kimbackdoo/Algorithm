# b에서 역으로 계산하여 a가 될때까지 반복, b가 a가 되는 순간 count + 1의 값을 출력 후 반환
# 만약 b가 a보다 작아지는 순간이 오면 b를 a로 만들 수 없다는 뜻이므로 -1 출력 후 반환
# 끝자리가 1이 아니고 홀수이면 어떠한 수든 b를 a로 바꿀 수 없으므로 -1 출력 후 반환
# 문자열로 처리하였지만 //10, %10 연산으로 활용 가능

# a, b = map(int, input().split())

# result = 0
# while True:
#   if a == b: # b가 a가 될때까지
#     print(result + 1)
#     break
#   elif a > b: # b를 a로 만들 수 없다면
#     print(-1)
#     break

#   if str(b)[-1] == "1": # 끝자리가 1이라면, 문자열로 변환후 마지막 수가 -1인지 체크
#     b = int(str(b)[:-1]) # 문자열 b에서 -1을 제외하고 int로 변환 
#     result += 1 # 횟수 count
#   else: # 끝자리가 1이 아니라면
#     if b % 2 == 0: # 그 중 짝수면 b에 2를 나누고 횟수 count
#       b //= 2
#       result += 1
#     else: # b가 홀수라면 어떠한 수든 a로 만들 수 없으므로 -1 출력 후 
#       print(-1)
#       break

# a -> b로 가는과정을 역으로 b -> a로 과정으로 생각, 주어진 조건 2개 중 하나를 선택해야 하므로 그리디 알고리즘 적용
a, b = map(int, input().split())

answer = 0
while a < b: # a가 b보다 작을경우에만 반복
  if b % 2 == 0: # b가 짝수면 나누기 2
    b //= 2
  else: # b가 홀수면
    tmp = str(b) # 문자열로 변환
    if tmp[-1] != "1": # 끝자리가 1이 아니면 a로 변환할 수 없으므로 break
      break
    b = int(tmp[:-1]) # 끝자리가 1이면 끝자리 1을 잘라내고 int로 변환
  
  answer += 1 # count

print((answer + 1) if a == b else -1)

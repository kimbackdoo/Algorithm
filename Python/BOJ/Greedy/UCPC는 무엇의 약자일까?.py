# 주어진 문자열을 적절하게 줄였을때 UCPC가 되면 됨
# 대소문자를 구별하므로 정확하게 UCPC 순서대로 줄여야함
# 즉, 줄였을 때 UPCC, PUCC, CUCP, ...이 되면 안됨
# 따라서 UCPC 순서대로 주어진 문자열에서 찾은 후 찾았으면 찾은 인덱스 이후로 문자열 슬라이싱
# 만약 못찾았으면 for문 종료하여 문자열을 UCPC로 줄일 수 있는지 없는지 확인

s = input()

check = True # 문자열을 UCPC로 줄일 수 있는지 확인하기 위한 변수
for alpha in "UCPC": # UCPC 순서대로 순회
  if s.find(alpha) != -1: # s에서 alpha를 찾으면
    s = s[s.find(alpha) + 1:] # 해당 요소 인덱스 이후로 문자열 슬라이싱
  else: # 못찾으면
    check = False # check False로 변환 후 break
    break

print("I love UCPC" if check else "I hate UCPC") # check가 True라는 의미는 UCPC로 줄일 수 있다는 의미이고, False는 UCPC로 줄일 수 없다는 의미

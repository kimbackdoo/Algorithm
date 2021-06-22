# 전화번호 목록을 정렬하게 되면 다음 전화번호가 현재 전화번호를 포함하는지 알 수 있음
# 예를 들어, [911, 97625999, 91125426] 리스트를 정렬하면 [911, 91125426, 97625999]가 되므로 911이 다른 전화번호의 접두어인지 확인하려면 바로 다음 전화번호를 확인하면 됨

t = int(input())
for _ in range(t):
  n = int(input())

  phones = []
  for _ in range(n):
    phones.append(input())

  phones.sort() # 한 번호가 다른 번호의 접두어인지 확인하기 위해 정렬
  check = False
  for i in range(len(phones)-1):
    if phones[i+1].find(phones[i]) == 0: # find 함수를 이용하여 접두어인지 확인, 접두어면 find 함수 반환값이 0이 나와야 한다.
      check = True # 접두어이면 일관성이 없는 것이므로 check 값을 True로 변경
      break

  if check: print("NO") # check가 True면 일관성이 없는 것이므로 NO 출력
  else: print("YES") # 아니면 YES 출력

# 버튼 A, B, C를 누른 횟수가 최소가 되어야 하므로 제일 큰 A 버튼부터 나누어야 한다, 즉, 그리디 알고리즘
# A 5분, B 1분, C 10초 그리고 t가 초 단위로 주어지므로 분으로 모두 초로 변환하여 계산한다.

t = int(input())

button = [300, 60, 10] # 각 버튼에 해당하는 초
abc = [0, 0, 0] # 각 버튼들이 몇번 눌렸는지 count하기 위한 리스트
for i in range(3):
  if t // button[i] != 0: # t를 각 버튼으로 나누었을 때 몫이 있다면
    abc[i] += (t // button[i]) # 몫이 해당 버튼을 누른 횟수이다
    t %= button[i] # 누르고 난 다음 t는 나누었을 때 나머지가 됨

if t != 0:
  print(-1)
else:
  for i in range(3):
    print(abc[i], end=" ")

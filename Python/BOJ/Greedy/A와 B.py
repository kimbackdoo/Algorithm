# s를 t로 변환하는 것과 t를 s로 변환시키는 것은 똑같음
# 따라서 t에서 A를 제거하거나 t에서 B를 제거하고 reverse하면 됨, 그리디 알고리즘 적용
# 역으로 생각하는 것도 중요! 항상 체크할 것!

s = list(input())
t = list(input())

while t: # t가 비어있지 않을 때까지 반복
  if t[-1] == "A": # t 마지막 값이 A라면
    t.pop() # A 제거
  else: # t 마지막 값이 B라면
    t.pop() # B 제거
    t.reverse() # reverse

  if s == t: # s와 t가 같다면 break
    break

print(1) if len(t) != 0 else print(0)

# s를 t로 변환하는 것과 t를 s로 변환시키는 것은 똑같음
# 따라서 t에서 A를 제거하거나 t에서 B를 제거하고 reverse하면 됨, 그리디 알고리즘 적용
# 역으로 생각하는 것도 중요! 항상 체크할 것!

# s = list(input())
# t = list(input())

# while t: # t가 비어있지 않을 때까지 반복
#   if t[-1] == "A": # t 마지막 값이 A라면
#     t.pop() # A 제거
#   else: # t 마지막 값이 B라면
#     t.pop() # B 제거
#     t.reverse() # reverse

#   if s == t: # s와 t가 같다면 break
#     break

# print(1) if len(t) != 0 else print(0)

# 문제에서 주어진 2개의 연산 중 그때그때마다 적절한 연산을 선택해야 하므로 그리디 알고리즘 적용

s, t = input(), input()

while len(t) != len(s): # s와 t의 길이가 같아질때까지 반복
  if t[-1] == "A": t = t[:-1] # t의 마지막 요소가 A일 경우 마지막 요소만 잘라냄
  else: t = t[:-1][::-1] # t의 마지막 요소가 B일 경우 마지막 요소를 잘라내고 뒤집음

print(1 if t == s else 0) # s와 t가 같다면 1 다르면 0 출력

# ord : 문자를 아스키코드 값으로 바꾸는 내장함수

start = input()

column = ord(start[0]) - ord('a') + 1
row = int(start[1])

steps = [(2,1), (2,-1), (-2,1), (-2,-1), (1,2), (1,-2), (-1,2), (-1,-2)]

result = 0
for step in steps:
  nextRow = row + step[0]
  nextColumn = column + step[1]

  if nextRow>=1 and nextRow<=8 and nextColumn>=1 and nextColumn<=8:
    result += 1

print(result)mud
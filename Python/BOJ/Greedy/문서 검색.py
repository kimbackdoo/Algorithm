# s에서 word를 찾은 후 찾지 못할 때까지 split 연산을 반복
# find 함수 이용

s = input()
word = input()

result = 0
while True:
  if s.find(word) == -1: # word를 찾지 못할 때까지 반복
    break
  # find 함수를 이용하여 문자를 찾은 위치부터 word의 길의 합을 split, 이유는 문자열의 시작위치가 아닌 끝 위치로 split 해야 하기 때문
  # 예를 들어 s: ababababa, word: aba라면
  # s: ababababa, s: bababa, s: ba 순으로 반복됨
  s = s[s.find(word) + len(word):]
  result += 1

print(result)

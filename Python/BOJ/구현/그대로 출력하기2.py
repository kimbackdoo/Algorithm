# 입력은 최대 100줄
# 입력은 알파벳 소문자, 대문자, 공백, 숫자로만 이루어져 있고, 만약 일반적인 문자열이 아닌 ctrl+d 와 같은 EOF를 의미하는 문자를 입력 받았을 경우 예외 처리를 해주어야 함 

for _ in range(100):
  try:
    print(input())
  except EOFError: # EOF 예외 처리
    continue

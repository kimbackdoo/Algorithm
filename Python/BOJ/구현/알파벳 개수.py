# 알파벳 개수가 26개 이므로 크기가 26인 리스트를 선언 및 0으로 초기화

s = input()

alpha = [0] * 26
for word in s:
  alpha[ord(word) - ord("a")] += 1 # ord 함수를 이용하여 s의 각 원소에 해당하는 alpha 인덱스 count

print(" ".join(map(str, alpha)))

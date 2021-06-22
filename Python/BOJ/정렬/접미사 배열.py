# s의 길이만큼 반복문을 순회하면서 인덱스 별로 split 후 오름차순 정렬

s = input()

strings = []
for i in range(len(s)):
  strings.append(s[i:]) # 인덱스 별로 정렬 즉, s[0:], s[1:], s[2:], ... , s[len(s)-1:]

for word in sorted(strings): # 오름차순 정렬 후 출력
  print(word)

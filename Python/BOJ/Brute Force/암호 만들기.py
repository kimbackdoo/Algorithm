# 암호는 최소 한 개의 모음과  최소 두 개의 자음을 포함하고 있어야 함
# 암호는 정렬되어 있어야 함
# 입력 받은 알파벳 리스트를 오름차순 정렬 후 L개 만큼 뽑한 조합 경우의 수를 구함
# 이렇게 하면 조합의 모든 경우들도 오름차순 정렬되어 있음
# 각각의 경우에 대해 모음의 개수를 구하고 모음의 개수가 1보다 크거나 같고 l-2보다 작거나 같은 경우는 암호에 해당할 수 있음

from itertools import combinations

l, c = map(int, input().split())
words = sorted(input().split()) # 입력 받은 알파벳들을 정렬하여 리스트로 만듦

vowel = ["a", "e", "i", "o", "u"]
for word in list(map("".join, combinations(words, l))): # words에서 l만큼 뽑는 조합을 구한 후 모든 조합 반복
  count = sum([1 for alpha in word if alpha in vowel]) # 해당 경우에서 모음의 개수 count
  
  # 1 <= count <= l-2인 이유는 암호에서 모음을 제외하면 전부 자음, 모음은 최소 1개, 자음은 최소 2개이므로
  if 1 <= count <= l-2: # 모음의 개수가 1보다 크거나 같고 l-2보다 작거나 같으면 암호에 해당할 수 있음
    print(word)

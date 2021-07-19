# 메모장에 적힌 키워드에 대한 keyword 집합 생성
# 새로운 글을 쓸 때 사용한 키워드 write 집합 생성
# keyword와 wirte의 차집합을 구한 후 길이가 정답

import sys
input = sys.stdin.readline
output = sys.stdout.write

n, m = map(int, input().split())

keyword = set()
for _ in range(n):
  keyword.add(input().rstrip()) # 메모장에 적힌 키워드에 대한 집합

for _ in range(m):
  write = set(input().rstrip().split(",")) # 새로운 글을 쓸 때 사용한 키워드 집합
  
  # keyword와 write의 차집합을 했을 때 keyword에 남아 있는 키워드들의 개수가 정답이 됨
  # 한 번 글을 쓰면 메모장에서 해당 키워드는 지워지게 되므로 keyword에서 새로운 글을 작성할 때마다 -= 연산을 통해 차집합을 
  keyword -= write
  output(f'{len(keyword)}\n')

# 서류 성적이 제일 높은 사람은 선발 따라서 입력받은 (서류 성적, 면접 성적) 리스트를 오름차순 정렬 후 첫 번째 요소는 무조건 선발
# 이후 면접 성적이 그 전 선발된 사람보다 높으면 선발됨 

t = int(input())
for _ in range(t):
  n = int(input())

  score = []
  for _ in range(n):
    paper, interview = map(int, input().split())
    score.append((paper, interview))

  score.sort() # (서류 성적, 면접 성적) 리스트 오름차순
  rank = score[0][1] # 첫 번째 선발된 사람 면접 성적 저장
  result = 1 # 첫 번째 사람은 선발되었으므로 1부터 count
  for i in range(1, n):
    if score[i][1] < rank: # 선발된 사람보다 면접 성적이 높을 경우 선발
      rank = score[i][1] # 다른 사람의 성적을 계속 확인해야 하므로 rank 값을 선발된 사람의 면접 성적으로 저장 
      result += 1 # count

  print(result)

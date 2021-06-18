# 파이썬 리스트를 이용하여 큐 구현
# 입력받은 문서 중요도 리스트를 인덱스와 묶어서 queue 리스트에 저장
# 이후 문제 조건에 따라 실행

t = int(input())
for _ in range(t):
  n, m = map(int, input().split())
  document = list(map(int, input().split()))

  queue = []
  for idx, priority in enumerate(document): # 문서 중요도 리스트와 인덱스를 enumerate를 이용하여 묶음
    queue.append((priority, idx))

  p = queue[m][1] # 찾고자 하는 문서를 p에 저장
  cnt = 0
  while queue: # 큐가 빌 때까지 반복
    if queue[0][0] < max(document): # 현재 문서 즉, 큐의 제일 앞 문서보다 중요도가 높은 문서가 하나라도 있다면
      queue.append(queue.pop(0)) # 현재문서를 제일 뒤로 보냄
    else: # 그렇지 않다면
      document.remove(max(document)) # document 리스트에서 max(document) 값 remove, 제일 중요도가 높은 문서를 제거해야 다른 문서를 비교할 수 있기 때문
      tmp = queue.pop(0) # queuue에서 제일 앞 요소 pop 즉, 바로 프린터
      cnt += 1
      if p == tmp[1]: # 만일 찾고자 하는 문서라면
        break # 반복 종료

  print(cnt)

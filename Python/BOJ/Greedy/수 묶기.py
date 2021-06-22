# 수가 양수일 때는 큰수끼리 묶고, 음수일 때는 작은 수끼지 묶으면 최대 합이 나옴
# 여기서 음수일 때 최대한 -를 없애야 하므로 음수 리스트에 0도 포함시켜 -를 없앰
# 예를 들어, [-10, -9, -8, 0], [-10, -9, -8]을 보면 첫번째 리스트에서 최대합은 90, 두번째 리스트에서 최대합은 82이므로 첫번째 리스트와 같이 0을 포함시켜 계산해야 최대합을 구할 수 있음

n = int(input())

pn, nn, rn = [], [], [] # pn: 양수, nn: 음수와 0, rn: 1
for _ in range(n):
  num = int(input())
  # num의 값에 따라 각각의 리스트에 저장
  if num > 1: pn.append(num)
  elif num <= 0: nn.append(num)
  else: rn.append(num)

result = 0
pn.sort(reverse=True) # 양수 리스트에서는 큰수부터 묶어야 하므로 역순 정렬
for i in range(0, len(pn), 2): # 수를 두개씩 묶기 위해 증가값 2
  if len(pn) % 2 == 1 and i == len(pn)-1: # pn의 개수가 홀수이고 i가 마지막 인덱스라면
    result += pn[i] # 마지막 값을 더함
    break
  result += (pn[i] * pn[i+1]) # result에 두개의 수를 곱한 값을 저장
  
nn.sort() # 음수일때는 작은 수부터 묶어야 하므로 오름차순 정렬
for i in range(0, len(nn), 2): # 수를 두개씩 묶기 위해 증가값 2
  if len(nn) % 2 == 1 and i == len(nn)-1: # nn의 개수가 홀수이고 i가 마지막 인덱스라면
    result += nn[i] # 마지막 값을 더함
    break
  result += (nn[i] * nn[i+1]) # result에 두개의 수를 곱한 값을 저장

result += sum(rn) # 마지막 1을 전부 더함
print(result)

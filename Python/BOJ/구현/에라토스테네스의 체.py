# 체로 걸러낸 리스트로 문제를 해결하는 것이 아닌 체로 거르는 과정에서 답을 구하면됨
# 따라서 체의 첫번째 for문의 범위가 n ** 0.5이 아닌 n으로 되어야 하고,
# 두번째 for문의 범위가 i * i부터 시작하는 것이 아닌 i로 되어야 함
n, k = map(int, input().split())

def seive(n, k): # 에라토스테네스의 체
  numbers = [0] * (n + 1) # 체 생성
  numbers[0] = numbers[1] = 1 # 0, 1은 소수가 아니므로 1로 저장
  for i in range(2, n + 1): # 2 ~ n까지 반복, 이때 2 ~ int((n + 1) ** 0.5) + 1이 아닌 것에 주의
    if not numbers[i]: # 아직 방문하지 않았으면 즉, 소수면
      for j in range(i, n + 1, i): # i ~ (n + 1)까지 i의 배수번 반복, 이때 (i * i) ~ (n + 1)이 아닌 것에 주의
        if not numbers[j]: # 아직 방문하지 않았으면 즉, 아직 체로 걸러지지 않았으면
          numbers[j] = 1 # 지움
          k -= 1 # count
          if not k: # k번째 지우는 숫자면
            return j # return
  
  return j # 만약 끝까지 다 지웠는데 k가 남았으면 j return

print(seive(n, k))

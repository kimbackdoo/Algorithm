# 입력받은 numbers에서 값을 하나하나 비교하면서 제일 큰 수로 만들어 나감, 그리디 알고리즘

n, k = map(int, input().split())
numbers = input()

stack = []
for num in numbers:
  while stack and stack[-1] < num and k > 0: # stack이 비어있지 않고, stack의 마지막 값이 num보다 작고, k가 0보다 크면 즉, 더 큰 수를 만들 수 있을때까지 반복
    stack.pop() # 그런 경우라면 pop
    k -= 1 # k 값 -1 감소
  
  stack.append(num)

if k > 0: # for문이 끝났는데 k가 0보다 크다면
  stack = stack[:-k] # numbers에서 k개의 숫자를 제거해야 하므로 뒤에서부터 -k 만큼 split 하여 작은 수 제거

print("".join(map(str, stack)))

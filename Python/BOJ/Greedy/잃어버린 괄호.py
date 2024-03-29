# "-" 이후 다음 "-"까지 괄호로 묶어서 계산하게 되면 최솟값을 구할 수 있음, 그리디 알고리즘 적용
# 예를 들어, 입력 받은 표현식이 "55-50+40-20"라면 "55 - (50 + 40) - 20"으로 괄호를 사용하면 최솟값이 됨

# expr = input().split("-") # 입력받은 표현식을 "-"를 기준으로 split 하여 리스트로 만듦
# for i in range(len(expr)): # 모든 리스트 요소에 대하여 반복
#   # "-"를 기준으로 split 하였기 때문에 expr 리스트에는 "+"와 숫자만 있게 된다.
#   # 따라서 모든 요소를 "+"를 기준으로 split 하여 합을 계산함
#   # 위 예시를 보면 expr에는 [55, 90, 20]이 담기게 됨
#   expr[i] = sum(map(int, expr[i].split("+")))

# result = expr[0] # 첫 번째 요소 이외의 값 전부를 - 연산하면 답을 도출할 수 있음
# for e in expr[1:]:
#   result -= e

# print(result)

expr = input().split("-")

result = sum(map(int, expr[0].split("+"))) # expr의 첫번째 요소 +를 기준으로 split 한 후 모든 요소 int로 변환 후 sum을 이용하여 더한 값을 result의 초기값으로 저장
for e in expr[1:]: # expr의 두번째 요소부터 전부 뺄셈해주면 됨
  result -= sum(map(int, e.split("+")))

print(result)

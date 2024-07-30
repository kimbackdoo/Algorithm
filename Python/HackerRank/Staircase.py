def staircase(n):
    for i in range(n):
        for j in range(i+1):
            if j==0:
                print(" "*(n-1-i), end="")
            print("#", end="")
        print()

# 코드의 시간 복잡도가 높아 코드 수정
# rjust : 오른쪽 정렬해주는 함수
def staircase(n):
    for i in range(1, n+1):
        print(str("#"*i).rjust(n))

# 다른 방법으로 코드 수정
def staircase(n):
  for i in range(n):
      print(" "*(n-1-i) + "#"*(i+1))
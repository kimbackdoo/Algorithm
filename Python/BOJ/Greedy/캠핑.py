# v에서 p를 계속해서 빼나가면 되므로 그리디
# v-p가 0보다 클 경우 v에서 p를 빼고 result에 l 값을 더함
# 그렇지 않으면 즉, 휴가를 다 썼으면 result에 v, l의 최솟값을 더함
# 이유는 v가 l보다 클 경우, l만큼 사용할 수 있으므로, v가 l보다 작으면 v만큼 사용하면 됨
# 예를 들어, l=2, p=7, v=20인 경우 14일 동안 4일 캠핑장을 이용할 수 있고 6일이 남았지만 그중 2일만 캠핑장을 이용할 수 있다.

# idx = 0
# while True:
#   l, p, v = map(int, input().split())

#   if l==0 and p==0 and v==0:
#     break

#   result = 0
#   while True:
#     if v-p > 0: # v-p가 0보다 클 경우 반복
#       v -= p
#       result += l
#     else: # 작을경우 즉, 휴가를 다 쓴 경우
#       result += min(v, l) # v, l 중 최솟값을 result에 더함
#       break

#   idx += 1
#   print("Case " + str(idx) + ": " + str(result))

# while 문을 사용하지 않고 수식으로 계산할 수 있음
# 연속하는 p일 중 l일만 캠핑장을 사용할 수 있고, 휴가일 수는 v일임
# 따라서 v // p 중 l일만 캠핑장을 사용할 수 있고, 남은 v % p일 중 l일만 캠핑장을 사용할 수 있음
import sys
input = sys.stdin.readline

index = 0
while True:
  l, p, v = map(int, input().split())
  if l == 0:
    break

  index += 1
  print("Case %d: %d" % (index, (l * (v // p) + min(l, (v % p))))) # 수식으로 계산, 문자열 formatting 이용하여 출력

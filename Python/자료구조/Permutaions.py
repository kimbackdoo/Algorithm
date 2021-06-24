# 다시 볼 것..

def permutations(arr, n):
  result = []
  if n == 0:
    return [[]]
    
  for i, elem in enumerate(arr):
    for p in permutations(arr[:i] + arr[i+1:], n-1):
      result += [[elem] + p]
      
  return result

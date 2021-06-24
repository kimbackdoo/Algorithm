# 다시 볼 것..

def combinations(arr, n):
  result =[]
  if n == 0:
    return [[]]

  for i in range(len(arr)):
    elem = arr[i]
    rest_arr = arr[i + 1:]
    for c in combinations(rest_arr, n-1):
      result.append([elem] + c)
      
  return result

def merge_sort(arr):
  if len(arr) <= 1:
      return arr

  mid = len(arr) // 2
  left_side = merge_sort(arr[:mid])
  right_side = merge_sort(arr[mid:])

  merged_arr = []
  left = right = 0
  while left < len(left_side) and right < len(right_side):
    if left_side[left] < right_side[right]:
      merged_arr.append(left_side[left])
      left += 1
    else:
      merged_arr.append(right_side[right])
      right += 1
  
  merged_arr += left_side[left:]
  merged_arr += right_side[right:]

  return merged_arr

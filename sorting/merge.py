# My merge-sort
def merge_sort(list):
  if len(list) <= 1:
    return list

  left_list = merge_sort(list[0:len(list)//2])
  right_list = merge_sort(list[len(list)//2:len(list)])

  return merge(left_list, right_list)


def merge(list_a, list_b):
  left, right, i = 0, 0, 0
  total_elements = len(list_a) + len(list_b)
  new_list = [0] * (total_elements)

  while (i < len(list_a) or i < len(list_b)):
    if (list_a[left] > list_b[right]):
      new_list[i] = list_b[right]
      right += 1
    else:
      new_list[i] = list_a[left]
      left += 1
    i += 1
  
  while left < len(list_a):
    new_list[i] = list_a[left]
    left += 1
    i += 1
  while right < len(list_b):
    new_list[i] = list_b[right]
    right += 1
    i += 1
  return new_list
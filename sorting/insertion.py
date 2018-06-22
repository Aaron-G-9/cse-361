
# My insertion Sort
def insertion_sort(list):
  for index in range(1, len(list)):
    value = list[index]
    temp_index = index
    for j in range(index -1, -1, -1):
      if (value < list[j]):
        list[temp_index], list[j] = list[j], list[temp_index]
        temp_index -= 1
      else:
        break
  return list

# Book Insertion Sort
def book_insertion_sort(list):
  for j in range(2, len(list)):
    key = list[j]
    i = j - 1
    while i > 0 and list[i] > key:
      list[i + 1] = list[i]
      i -= 1
    list[i + 1] = key
  return list
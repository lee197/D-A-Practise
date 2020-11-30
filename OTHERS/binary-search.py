class BinarySearch: 
  def __init__(self, arr):
    self.arr = arr
    self.count = len(arr)

  def iterative_binary_search(self, target):
    s = 0
    e = self.count - 1

    while s <= e:
      mid = int(e - (e-s)/2)
      if self.arr[mid] == target:
        return mid
      elif self.arr[mid] < target:
        s = mid + 1
      else:
        e = mid - 1

    return -1

  def recursion_binary_search(self, target):
    s = 0
    e = self.count - 1
    return self.__recursionBinarySearch(s, e, target)

  def __recursionBinarySearch(self, s, e, target):
    if s > e:
      return -1
    mid = int(e - (e-s)/2)

    if self.arr[mid] == target:
      return mid
    elif self.arr[mid] < target:
      return self.__recursionBinarySearch(mid + 1, e, target)
    else:
      return self.__recursionBinarySearch(s, mid - 1, target)


arr = [1,2,3,4,5,6,7,8,9]
binary_search = BinarySearch(arr)
print(binary_search.iterativeBinarySearch(2))
print(binary_search.recursionBinarySearch(2))

print(binary_search.iterativeBinarySearch(9))
print(binary_search.recursionBinarySearch(9))

print(binary_search.iterativeBinarySearch(10))
print(binary_search.recursionBinarySearch(10))

print(binary_search.iterativeBinarySearch(7))
print(binary_search.recursionBinarySearch(7))
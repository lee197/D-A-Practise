class Heap:

  def __init__(self, arr):
    self.arr = []
    self.arr.append(-1)
    for i in range(len(arr)):
      self.arr.append(arr[i])

    for item in range(1, int((len(self.arr) - 1 )/2)):
      self.__shiftDown(item)

  def print_heap(self):
    print(self.arr)

  def isEmpty():
    return len(self.arr) - 1 == 0
  
  def size():
    return len(self.arr) - 1

  def add(self, val):
    self.arr.append(val)
    self.__shiftUp()

  def remove(self):
    self.arr[1], self.arr[- 1] = self.arr[- 1], self.arr[1]
    val = self.arr.pop(-1)
    self.__shiftDown(1)
    return val
    
  def __shiftUp(self):
    k = len(self.arr) - 1
    while k > 1 and self.arr[k/2] < self.arr[k]:
      self.arr[k/2], self.arr[k] = self.arr[k], self.arr[k/2]
      k /= 2

  def __shiftDown(self, k):
    count = len(self.arr) - 1
    print(k)
  
    while 2*k < count:
      j = 2*k
      if j + 1 <= count and self.arr[j+1] > self.arr[j]:
        j += 1
      if self.arr[k] >= self.arr[j]:
        break
      self.arr[k], self.arr[j] = self.arr[j], self.arr[k]
      k = j


import random

randomlist = random.sample(range(0, 50), 10)
print(randomlist)
heap = Heap(randomlist)
heap.print_heap()
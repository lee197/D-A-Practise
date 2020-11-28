class Heap:

  def __init__(self, arr):
    self.arr = []
    self.arr.append(-1)
    for i in range(len(arr)):
      self.arr.append(arr[i])
    self.count = len(arr)
    for i in range(int(self.count/2), 0, -1):
      self.__shiftDown(i)

  def isEmpty(self):
    return self.count == 0
  
  def size(self):
    return self.count

  def add(self, val):
    self.arr.append(val)
    self.count += 1
    self.__shiftUp(self.count)

  def remove(self):
    self.arr[1], self.arr[- 1] = self.arr[- 1], self.arr[1]
    val = self.arr.pop(-1)
    self.count -= 1
    self.__shiftDown(1)
    return val
    
  def __shiftUp(self, k):
    while k > 1 and self.arr[int(k/2)] < self.arr[k]:
      self.arr[k/2], self.arr[k] = self.arr[k], self.arr[k/2]
      k /= 2

  def __shiftDown(self, k):
    
    while 2*k <= self.count:
      j = 2*k
      if j + 1 <= self.count and self.arr[j+1] > self.arr[j]:
        j += 1
      if self.arr[k] >= self.arr[j]:
        break
      self.arr[k], self.arr[j] = self.arr[j], self.arr[k]
      k = j


import random

randomlist = random.sample(range(0, 50), 10)
print("Initial radom: " + str(randomlist))

heap = Heap(randomlist)
print("After heapify: " + str(heap.arr))

heap.add(20)
print("After added: " + str(heap.arr))

heap.remove()
print("After removed: " + str(heap.arr))

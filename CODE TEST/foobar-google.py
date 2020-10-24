# def solution(x):
#     result = ""
    
#     for item in x:
#         ascii_num = ord(item)
#         if ascii_num < 97 or ascii_num > 122:
#             result += item
#         else:
#             gap = ascii_num - 97
#             result += chr(122-gap)
#     return result

# print(solution("wrw blf hvv ozhg mrtsg'h vkrhlwv?"))

# import heapq

# def solution(l):
#     versions_str = [item.split(".") for item in l]
#     versions_int = [list(map(int,item)) for item in versions_str]
#     heapq.heapify(versions_int)
#     result = []

#     while versions_int:
#       version_int = heapq.heappop(versions_int)
#       arr_str = '.'.join(str(num) for num in version_int)
#       result.append(arr_str)
#     return result



# print(solution(['1.2.3','9.3.4','5.6.7','2.8.2','5.4.6','5.4', '0.2','3.45']))
# print(solution(["1.11", "2.0.0", "1.2", "2", "0.1", "1.2.1", "1.1.1", "2.0"]))
# print(solution(["0.0.1", "1.0", "1.3.3", "1.0.12", "1.0.2","1.1.3.4.5.3.2.4.5"]))


# def solution(xs):
#     negitive_factor = -2000
#     multi_sum = 1
#     if len(xs) == 1 and arr[0] < 0:
#         return str(xs[0])
#     arr = list(filter(lambda x: x != 0, xs))
#     if len(arr) == 1 and arr[0] < 0 or len(arr) == 0:
#         return str(0)
        
#     for i in arr:
#          multi_sum *= i
#          if i < 0 and i > negitive_factor:
#             negitive_factor = i
#     if multi_sum < 0:
#         multi_sum //= negitive_factor
#     return str(multi_sum)

# print(solution([-2, -3, 4, -5]))
# print(solution([2, 0, 2, 2, 0]))
# print(solution([-2, -3, -4, -5, -7]))
# print(solution([-2, -3, 4, -5, 1]))
# print(solution([0, 0, 0, 0, 0, -8]))
# print(solution([0, 0, 0, 0, 0, 0]))
# print(solution([0, 0, 0, 0, 0, 11111]))
# print(solution([0, 0, 0, 0, -1, -1]))
# print(solution([]))

# print(solution([0]))
# print(solution([2]))
# print(solution([-2]))
# print(solution([0, 1000, -1000, 0, 0, -1]))
# print(1000 ** 50 > 2147483647)

# test = []
# for i in range(50):
#   test.append(1000)
# print(test)
# print(solution(test))



import numpy as np
from fractions import Fraction
from copy import deepcopy

# def create_absorb_matrix(matrix):
test = [
  [0,1,0,0,0,1],  # s0, the initial state, goes to s1 and s5 with equal probability
  [4,0,0,3,2,0],  # s1 can become s0, s3, or s4, but with different probabilities
  [0,0,0,0,0,0],  # s2 is terminal, and unreachable (never observed in practice)
  [0,0,0,0,0,0],  # s3 is terminal
  [0,0,0,0,0,0],  # s4 is terminal
  [0,0,0,0,0,0],  # s5 is terminal
]
def create_absortb_matrix(m):
  for i in range(len(m)):
    if sum(m[i]) == 0:
      m[i][i] = 1
  return m

def add_fraction(m):
  for i in range(len(m)):
    row_sum = sum(m[i])
    if row_sum != 0:
      for j in range(len(m[i])):
        if m[i][j] != 0:
          m[i][j] = Fraction(m[i][j], row_sum)

def convert_matrix(m):
  add_fraction(m)
  matrix = deepcopy(m)
  factor = 0
  for i in range(len(m)):
    row_sum = sum(m[i])

    if row_sum != 0:
      factor += 1
      convert_matirx_item(matrix,i)
  create_absortb_matrix(matrix)
  return break_matrix(matrix, len(m)-factor, factor)
      
def convert_matirx_item(m, i):

  m.append(m.pop(0))
  for row in m:
    row.append(row.pop(0))
  # print(m)


def break_matrix(matrix, index, factor):
  m = matrix
  n = len(m)
  I = []
  R = []
  Q = []

  for i in range(n):
    if i < index:
      temp_array = []
      for j in range(index):
        temp_array.append(m[i][j])
      I.append(temp_array)
    else:
      temp_array = []
      temp_array1 = []
      for h in range(n):
        if h < index:
          temp_array.append(m[i][h])
        else:
          temp_array1.append(m[i][h])

      R.append(temp_array)
      Q.append(temp_array1)
  
  if index > factor:
    gap = index - factor
    for i in range(gap):
      I.pop()
    for j in I:
      for m in range(gap):
        j.pop()
  elif index < factor:
      gap = factor - index
      for j in I:
        for i in range(gap):
          j.append(0)
      m = len(I[0])
      for i in range(gap):
        temp = [0] * m
        temp[len(temp) - gap] = 1
        I.append(temp)






  return (R, Q, I)


  # print(R)
  # print(Q)
  # print(I)

def solution(m):
  blocks=convert_matrix(m)
  R = np.matrix(blocks[0])
  Q = np.matrix(blocks[1])
  I = np.matrix(blocks[2])
  print(R)
  print(Q)
  print(I)

  print(I-Q)






  
# convert_matrix(test)

print(solution(test))



# import numpy as np

# a = np.array([[4,3,1], [5,7,0], [9,9,3], [8,2,4]])

# print(a)
 
# # array([[4, 3, 1],
# #        [5, 7, 0],
# #        [9, 9, 3],
# #        [8, 2, 4]])

# a[[0, 2]] = a[[2, 0]]
# print(a)
# # array([[9, 9, 3],
# #       [5, 7, 0],
# #       [4, 3, 1],
# #       [8, 2, 4]])
    


   

# def solution(m):

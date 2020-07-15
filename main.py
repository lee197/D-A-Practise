class Solution:
  def __init__(self, input):
    self.__input = input
  
  def findRanges(self) -> []:
    num = self.__input
    count = len(num)

    if count == 0:
      return []

    if count == 1:
      return [str(num[0]) + "->" + str(num[0])]

    result = []
    end = 0
    index = 1
    start = index - 1

    while True:
      if index == count: 
          result.append(str(num[start]) + "->" + str(num[index-1]))
          break


      if num[index] - num[index-1] != 1:
        end = index - 1
        result.append(str(num[start]) + "->" + str(num[end]))
        start = index

      index+=1

    return result

solution = Solution([1,2,3,4,8,9,10,79])
print(solution.findRanges())
  


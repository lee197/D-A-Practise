# A string s is called good if there are no two different characters in s that have the same frequency.
# Given a string s, return the minimum number of characters you need to delete to make s good.
# The frequency of a character in a string is the number of times it appears in the string. 
# For example, in the string "aab", the frequency of 'a' is 2, while the frequency of 'b' is 1.

# Example 1:

# Input: s = "aab"
# Output: 0
# Explanation: s is already good.

# Example 2:

# Input: s = "aaabbbcc"
# Output: 2
# Explanation: You can delete two 'b's resulting in the good string "aaabcc".
# Another way it to delete one 'b' and one 'c' resulting in the good string "aaabbc".

# Example 3:

# Input: s = "ceabaacb"
# Output: 2
# Explanation: You can delete both 'c's resulting in the good string "eabaab".
# Note that we only care about characters that are still in the string at the end (i.e. frequency of 0 is ignored).

# Constraints:

# 1 <= s.length <= 105
# s contains only lowercase English letters.
from collections import Counter

class Solution1: 
  def minDeletion(self, s):
    cnt = Counter(s)
    used = set()
    res = 0

    for char, freq in cnt.items():
      while freq in used:
        freq -= 1
        res += 1
      used.add(freq)
    return res

solution = Solution1()
sampleS1 = "ceabaacb"
sampleS2 = "daaabbbcc"
sampleS3 = "aab"

print(solution.minDeletion(sampleS1))
print(solution.minDeletion(sampleS2))
print(solution.minDeletion(sampleS3))


# Given a string, what is the minimum number of adjacent swaps required to convert a string into a palindrome. 
# If not possible, return -1.

# Example 1:

# Input: "mamad"
# Output: 3

# Example 2:

# Input: "asflkj"
# Output: -1

# Example 3:

# Input: "aabb"
# Output: 2

# Example 4:

# Input: "ntiin"
# Output: 1

# Explanation: swap 't' with 'i' => "nitin"

# PLEASE NOTE IT'S ADJACENT swaps

class Solution2:

  def isValidPalindrome(self, s):
    cnt = Counter(s)
    isValidCounter = 0
    for item, freq in cnt.items(): 
      if freq % 2 != 0:
        isValidCounter += 1
    if isValidCounter > 1:
      return False
    else:
      return True

  def min_swaps(self, s):

    if not self.isValidPalindrome(s):
      return -1

    s = list(s)
    f = 0 
    b = len(s) - 1
    res = 0

    while b > f:
      if s[b] != s[f]:
        mid = b
        while mid > f and s[f] != s[mid]: 
          mid -= 1

        if mid == f:
          s[mid], s[mid + 1] = s[mid + 1], s[mid]
          res += 1
          continue

        for i in range(mid, b):
          s[i], s[i + 1] = s[i + 1], s[i]
          res += 1

      b -= 1
      f += 1
    return res
    
solution = Solution2()

print(solution.min_swaps("mamad") == 3)
print(solution.min_swaps("asdgfr") == -1)
print(solution.min_swaps("aabb") == 2)
print(solution.min_swaps("ntiin") == 1)

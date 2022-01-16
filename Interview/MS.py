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
        return len([char for char, freq in cnt.items() if freq % 2]) <= 1

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

# Alexa is given n piles of equal or unequal heights. In one step, Alexa can remove any number of boxes from the pile which has the maximum height and try to make it equal to the one which is just lower than the maximum height of the stack. Determine the minimum number of steps required to make all of the piles equal in height.

# Example 1:

# Input: piles = [5, 2, 1]
# Output: 3
# Explanation:
# Step 1: reducing 5 -> 2 [2, 2, 1]
# Step 2: reducing 2 -> 1 [2, 1, 1]
# Step 3: reducing 2 -> 1 [1, 1, 1]
# So final number of steps required is 3.

# Let's take an example.
# Input  : [1, 1, 2, 2, 2, 3, 3, 3, 4, 4]
# Output : 15
# After sorting in reverse, we have...
# [4, 4, 3, 3, 3, 2, 2, 2, 1] --> (2 steps to transform the 4's) --> The 3's must wait for 2 numbers before it to finish their reduction
# [3, 3, 3, 3, 3, 2, 2, 2, 1] --> (5 steps to transform the 3's) --> The 2's must wait for 5 numbers before it to finish their reduction
# [2, 2, 2, 2, 2, 2, 2, 2, 1] --> (8 steps to transform the 2's) --> The 1's must wait for 8 numbers before it to finish their reduction
# [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]

# Why did we sort in reverse? Because we want to process the maximum / largest number(s) first, which is what the question wants. At each step, we can only reduce the largest number(s) to the value of the 2nd-largest number(s)

# The main idea throughout the algorithm is that - Every time I meet a different number in the reverse-sorted array, I have to count how many numbers came before it. This represents the number of steps that was taken to reduce these numbers to the current number


class Solution3:
    def reducing_steps(self, piles):
        if len(piles) == 1:
            return 0

        piles = sorted(piles, reverse=True)
        i = 1
        res = 0
        while i < len(piles):
            if piles[i - 1] != piles[i]:
                res += i
            i += 1
        return res


solution = Solution3()
print(solution.reducing_steps([1, 1, 2, 2, 2, 3, 3, 3, 4, 4]) == 15)

print(solution.reducing_steps([5, 2, 1]) == 3)
print(solution.reducing_steps([5, 2, 1, 4, 4, 8, 8]) == 16)

# Write a function that, given an array A of N integers, returns the lagest integer K > 0 such that both values K and -K exist in array A.
# If there is no such integer, the function should return 0.

# Example 1:

# Input: [3, 2, -2, 5, -3]
# Output: 3
# Example 2:

# Input: [1, 2, 3, -4]
# Output: 0

# Approaches:

# Sorting + Two Pointers O(nlogn)
# Array: [3,2,-2,5,-3]
# After Sorting:[-3,-2,2,3,5]
# Keep two pointers on the 0th and the last position respectively,
# while(left<right) // To avoid zero's case
# 1)if the absolute values match, return the value
# 2) right--, if right's absolute value is greater than left's value
# 3)left++, if left's absolute value is greater than right's value

# Extra Space O(n)
# Use an Array/HashMap to keep the occurences of the element, save the absolute value in the array/hashmap.
# whenever you already have your absolute value in the map, compare it with the ans variable and take the maximum out of the two.


class Solution4:
    def find_largest(self, arr):
        arr = sorted(arr)
        f = 0
        b = len(arr) - 1

        while f < b:
            if abs(arr[f]) == arr[b]:
                return arr[b]
            elif arr[b] > abs(arr[f]):
                b -= 1
            else:
                f += 1
        return 0


solution = Solution4()
print(solution.find_largest([3, 2, -2, 5, -3]) == 3)
print(solution.find_largest([1, 2, 3, -4, -5]) == 0)

# You are given an array of strings arr. A string s is formed by the concatenation of a subsequence of arr that has unique characters.

# Return the maximum possible length of s.

# A subsequence is an array that can be derived from another array by deleting some or no elements without changing the order of the remaining elements.

# Example 1:

# Input: arr = ["un","iq","ue"]
# Output: 4
# Explanation: All the valid concatenations are:
# - ""
# - "un"
# - "iq"
# - "ue"
# - "uniq" ("un" + "iq")
# - "ique" ("iq" + "ue")
# Maximum length is 4.
# Example 2:

# Input: arr = ["cha","r","act","ers"]
# Output: 6
# Explanation: Possible longest valid concatenations are "chaers" ("cha" + "ers") and "acters" ("act" + "ers").
# Example 3:

# Input: arr = ["abcdefghijklmnopqrstuvwxyz"]
# Output: 26
# Explanation: The only string in arr has all 26 characters.

# Constraints:

# 1 <= arr.length <= 16
# 1 <= arr[i].length <= 26
# arr[i] contains only lowercase English letters.

# Explanation
# Initial the result res to include the case of empty string "".
# res include all possible combinations we find during we iterate the input.

# Itearte the the input strings,
# but skip the word that have duplicate characters.
# The examples is kind of misleading,
# but the input string can have duplicate characters,
# no need to considerate these strings.

# For each string,
# we check if it's conflit with the combination that we found.
# If they have intersection of characters, we skip it.
# If not, we append this new combination to result.

# return the maximum length from all combinations.


class Solution5:
    def len_concatenation(self, arr):
        def is_unique(s):
            cnt = Counter(s)
            if len(cnt) != len(s):
                return False
            else:
                return True

        res = 0
        arr.append("")

        for i in range(0, len(arr)):
            if len(set(arr[i])) < len(arr[i]): continue
            for j in range(i + 1, len(arr)):
                concat_str = arr[i] + arr[j]
                if is_unique(concat_str) and len(concat_str) > res:
                    res = len(concat_str)
        return res


solution = Solution5()

print(solution.len_concatenation(["cha", "r", "act", "ers"]) == 6)
print(solution.len_concatenation(["un", "iq", "ue"]) == 4)
print(solution.len_concatenation(["un", "iq"]) == 4)

print(solution.len_concatenation(["abcdefghijklmnopqrstuvwxyz"]) == 26)

# Given an integer n, return any array containing n unique integers such that they add up to 0.

# Example 1:

# Input: n = 5
# Output: [-7,-1,1,3,4]
# Explanation: These arrays also are accepted [-5,-1,1,2,3] , [-3,-1,2,-2,4].
# Example 2:

# Input: n = 3
# Output: [-1,0,1]
# Example 3:

# Input: n = 1
# Output: [0]

# Constraints:

# 1 <= n <= 1000

# Intuition
# Naive idea
# n = 1, [0]
# n = 2, [-1, 1]

# Now write more based on this
# n = 3, [-2, 0, 2]
# n = 4, [-3, -1, 1, 3]
# n = 5, [-4, -2, 0, 2, 4]

# It spreads like the wave.

# Explanation
# Find the rule
# A[i] = i * 2 - n + 1

# Math Observation
# @zzg_zzm helps explain in math.

# Actually, this rule could be derived from constructing an arithmetic sequence.

# (Note that any arithmetic sequence must have unique values if the common delta is non-zero)

# We need the sequence sum, so that

# (a[0] + a[n-1]) * n / 2 = 0, which means a[0] + a[n-1] = 0.

# Note that a[n-1] - a[0] = (n-1) * delta, which is -2 * a[0],

# so we simply set delta = 2, a[0] = 1 - n

# Note
# It's not bad to sum up 1 + 2 + 3 + ... + (N - 1).
# Personally I don't really like it much.
# What is the possible problem of this approach?
# It doesn't work if N goes up to 10^5


# Complexity
# Time O(N)
# Space O(N)
class Solution5:
    def sumZero(self, n):
        return list(range(1 - n, n, 2))


solution = Solution5()
print(solution.sumZero(6))
print(solution.sumZero(5))
print(solution.sumZero(1))

# Given an array of non-negative integers arr, you are initially positioned at start index of the array. When you are at index i, you can jump to i + arr[i] or i - arr[i], check if you can reach to any index with value 0.

# Notice that you can not jump outside of the array at any time.

 

# Example 1:

# Input: arr = [4,2,3,0,3,1,2], start = 5
# Output: true
# Explanation: 
# All possible ways to reach at index 3 with value 0 are: 
# index 5 -> index 4 -> index 1 -> index 3 
# index 5 -> index 6 -> index 4 -> index 1 -> index 3 
# Example 2:

# Input: arr = [4,2,3,0,3,1,2], start = 0
# Output: true 
# Explanation: 
# One possible way to reach at index 3 with value 0 is: 
# index 0 -> index 4 -> index 1 -> index 3
# Example 3:

# Input: arr = [3,0,2,1,2], start = 2
# Output: false
# Explanation: There is no way to reach at index 1 with value 0.
 

# Constraints:

# 1 <= arr.length <= 5 * 104
# 0 <= arr[i] < arr.length
# 0 <= start < arr.length

# Similar to what we did in the above solution, we can do it using BFS as well. The only difference in these two would be that BFS would be equivalent to exploring all possible paths till now at once (meaning one move at a time in each path), while DFS is equivalent to exploring one path at a time till we either completely explore it or reach the target index.

# We start by pushing the starting index into the queue and iteratively trying both possible jumps from indices in queue.

# If we A[cur] 0, we can return true.
# If we reach already visited index (A[cur] < 0), we discard further exploration of this path & continue to next element of queue
# If current index is not visited and value is not equal to 0, further explore both possible jumps from this index by pushing both of it into queue (after proper bounds check).
from collections import deque
class Solution5:
  def can_reach(self, arr, start):
    q = deque([start])
    while q:
      cur = q.popLeft()
      if arr[cur] == 0:
        return True
      if arr[cur] < 0: continue
      if cur + arr[cur] < len(arr): q.append(cur + arr[cur])
      if cur - arr[cur] >= 0: q.append(cur - arr[cur])

      arr[cur] *= -1
    return False



# Given an array of meeting time intervals intervals where intervals[i] = [starti, endi], return the minimum number of conference rooms required.

 

# Example 1:

# Input: intervals = [[0,30],[5,10],[15,20]]
# Output: 2
# Example 2:

# Input: intervals = [[7,10],[2,4]]
# Output: 1
 

# Constraints:

# 1 <= intervals.length <= 104
# 0 <= starti < endi <= 106
from collections import heapq
class Solution:
    def minMeetingRooms(self, intervals):
        
        if not intervals:
            return 0
        
        rooms = []
        intervals.sort(key = lambda x: x[0])
        heapq.heappush(rooms, intervals[0][1])
        
        for interval in intervals[1:]:
            if rooms[0] <= interval[0]:
                heapq.heappop(rooms)
            heapq.heappush(rooms, interval[1])
            
        return len(rooms)

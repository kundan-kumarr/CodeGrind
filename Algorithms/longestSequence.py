"""
1. Sort the array
2. Keep track of current length count (current) and longest length count (longest). Both starting at 1.
3. Loop through the sorted array 
4. Skip duplicates
5. If current number is one more than previous number, increment current streak 
6. Else set longest streak and reset current streak
7. Return the longest streak
"""
class Solution(object):
    def longest_sequence(self,nums):
        if not nums:
            return 0
        
        # Sort the array
        nums.sort()

        long_streak =1
        cur_streak =1
        for i in range(1,len(nums)):
            if nums[i] ==nums[i-1]:
                continue

            if nums[i] == nums[i-1]+1:
                cur_streak +=1

            else:
                long_streak =max(long_streak,cur_streak)
                cur_streak =1

        return max(long_streak,cur_streak)


print(Solution().longest_sequence([0,3,7,2,5,8,4,6,0,1]))

"""
using Hashing:
1. Keep track of longestStreak starting at 0.
2. Create a hashset 
3. Loop through the number set
4. If current number has no previous number, then start counting from this number
5. While the set contains currentNum + 1, increment currentNum and currentStreak
6. After each while loop, check and set longestStreak
7. Return longestStreak
"""

class Solution(object):
    def longestseq(self,nums):
        longest_streak =0
        hash_set = set(nums)

        for i in hash_set:
            if i-1 not in hash_set:
                current_num =i
                current_streak =1

                while current_num+1 in hash_set:
                    current_num +=1
                    current_streak +=1

                longest_streak=max(longest_streak,current_streak)

        return longest_streak

print(Solution().longestseq([0,3,7,2,5,8,4,6,0,1]))
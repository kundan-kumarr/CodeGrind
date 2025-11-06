"""Given an integer array nums, rotate the array to the right by k steps, where k is non-negative."""

"""
Method 1: Time Complexity : O(n^2), Space : O(1)
"""
class Solution(object):
    def rotate_array(self,nums,k):
        k %= len(nums)
        #print(k)
        for i in range(k):
            prev = nums[-1]
            for j in range(len(nums)):
                nums[j], prev = prev,nums[j]
                # print(nums[j])
                # print(prev)
        return nums

"""
Method 2: Time Complexity : O(n), Space : O(n)
"""

class Solution(object):
    def rotate_array(self,nums,k):

        n = len(nums)
        arr = [0]*n

        for i in range(n):
            arr[(i+k)%n] = nums[i]

        nums[:] = arr

        return nums

print(Solution().rotate_array([1,2,3,4,5,6,7],3))
print(Solution().rotate_array([-1,-100,3,99],2))


"""Given an integer array nums, rotate the array to the right by k steps, where k is non-negative."""

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


print(Solution().rotate_array([1,2,3,4,5,6,7],3))
print(Solution().rotate_array([-1,-100,3,99],2))
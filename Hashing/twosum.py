class Solution(object):
  def twoSum(self,nums,target):
    for i,a in enumerate(nums):
      for j,b in enumerate(nums):
        if a==b:
          continue
        else:
          if a+b ==target:
            return [i,j]
    return []

  def twoSumB(self,nums,target):
    val ={}
    for i, num in enumerate(nums):
      diff = target-num
      if diff in val:
        return [i,val[diff]]
      val[num] =i
    return []

    


print(Solution().twoSum([2, 7, 11, 15], 18))
print(Solution().twoSumB([2, 7, 11, 15], 18))


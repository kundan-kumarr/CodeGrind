class Solution(object):
    def duplicate(self,num):
        # Create Set
        dup=set()
        # Iterate through Number
        for i in num:
            
            # If number is already in set return True
            if i in dup:
                return True
            # Store number in set
            dup.add(i)
        return False

print(Solution().duplicate([1,1,1,3,3,4,3,2,4,2]))
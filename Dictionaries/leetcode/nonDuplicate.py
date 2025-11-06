"""
Find the non-duplicate number
for n in num:
    if not n in occur:
        occur[n] = 1
    else:
        occu[n] += 1
"""

class Solution(object):
    def nonduplicate(self,num):
        occur ={}
        for n in num:
            occur[n]=occur.get(n,0)+1

        for key,value in occur.items():
            if value==1:
                return key

    def nonduplicate(self,num):
        check =0
        for n in num:
            check^=n
        return check

print(Solution().nonduplicate([4, 3, 2, 4, 1, 3, 2]))

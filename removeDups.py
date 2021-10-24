
'''
remove the duplicates in-place such that each unique element appears only once. 
The relative order of the elements should be kept the same.

method 1: using a stack

'''


class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ct = 0
        stack = []

        # add only unique elements to the stack (in sorted order)
        for i in nums:
            if i in stack:
                continue
            else:
                stack.append(i)
                ct += 1
                
        # replace first "ct" elements in nums with elements from stack
        for i in range (ct-1, -1, -1):
            nums[i] = stack.pop()

        return ct





nums = [1, 1, 1, 2, 3, 3]

a = Solution()
b = a.removeDuplicates(nums)
print("Ans:", b)

for i in nums: 
    print(i)
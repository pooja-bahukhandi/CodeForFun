'''

Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. 
The relative order of the elements may be changed.

method: using stack

faster than 81.15% of Python online submissions for Remove Element
'''

class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """

        ct = 0
        stack = []

        # save all elements except val in the stack
        for i in nums:
            if i==val:
                continue
            else:
                stack.append(i)
                ct += 1

        # pop all elems of stack back into nums 
        for i in range(ct-1, -1, -1):
            nums[i] = stack.pop()
            print(i, nums[i])

        return ct


nums = [3,2,2,3]
val = 3

a = Solution()
b = a.removeElement(nums, val)

""" print(b)
for i in nums:
    print(i) """
# idea - bruteforce (37 ms)

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        x = range(len(nums))
        sum = 0
        current = 0
        current_index = 0
        final_list = []

        for i in nums :  # 11,22,33
            current = i
            current_index = nums.index(i)
            if (len(final_list) == 2) :
                break
            
            for j in nums : # 11,22,33
                
                if (current == j) : 
                    continue
                    
                sum = nums[current_index] + j
                if (sum == target) : 
                    final_list.append(current_index)
                    final_list.append(nums.index(j))

        return final_list
                    
                
# q - are elements unique? are duplciates allwoed?

nums = [11,22,33]
target = 33


obj_a = Solution()
f = obj_a.twoSum(nums, target)

for i in f : 
    print(i)

        
# idea - O(n) but faster method (25 ms)

# iterate through nums 
# fix x 
# search the list for (target - x)



class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        y = 0
        final_list = []
        c = 0

        for x in nums : 
            cur_index = nums.index(x)
            y = target - x 

            if (y == x) : 
                c = 1

            if ((y in nums) and (c==0))  :
                next_index = nums.index(y)

                final_list.append(cur_index)
                final_list.append(next_index)
                break
            elif (c == 1) :   # y and x are equal 
                print("here")
                nums[nums.index(x)] = -1
                if y in nums : # y is in the list 
                    next_index = nums.index(y)
                    final_list.append(cur_index)
                    final_list.append(next_index)
                    break
                else : # y is not in list 
                    nums[nums.index(-1)] = y
                    continue

            else :
                continue

        return final_list 



nums = [3,3]
target = 6

obj_a = Solution()
f = obj_a.twoSum(nums, target)

for i in f : 
    print(i)

             


             
'''

return longest common prefix from an array of strings

note: max length of prefix = length of smallest string in array

'''

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """

        # find smallest string in array 
        length = len(strs[0])
        ind = 0
        
        for i in range(0, len(strs)):
            temp_len = len(strs[i])

            if temp_len < length:
                length = temp_len
                ind = i

        smallestStr = strs[ind]
        tempSmallStr = smallestStr

        smallestLen = len(smallestStr)
        tempSmallLen = smallestLen

        flag = False

        # iterate through strs
        # slice each string from start_index = len(smallestStr) to end of string

        for i in range(0, tempSmallLen):

            for j in strs:

                if j[0:smallestLen] != smallestStr:
                    smallestLen -= 1
                    flag = True
                
                if flag: 
                    flag = False
                    break
                    

        return smallestLen
        
        

strs = ["abd", "abcd", "abcde"]
strs1 = ["flower","flight", "flow"]

a = Solution()
pref = a.longestCommonPrefix(strs)
print("Answer:", pref)
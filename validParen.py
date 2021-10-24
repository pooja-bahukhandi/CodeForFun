


class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """


        stack = []
        dict = {")": "(", 
                "}": "{", 
                "]": "[" }

        for i in s:
            if i in dict.values():
                stack.append(i)
            else:     # keys
                if stack == [] or dict[i] != stack.pop():
                    return False
            
        return stack == []






s = "({[]})"
s1 = ""
s3 = "({}"
s4 = "(]"
s5 = "()[]"

a = Solution()
b = a.isValid(s5)
print(b)
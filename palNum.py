

# return False if x < 0 else x == int(str(x)[::-1])


class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        ans = False

        if (x < 0) :
            return ans
        
        res = 0
        c = 0
        x_dup = x

        upper = pow(2,31) - 1
        lower = (-1) * pow(2,31)

        if (x < 0) : 
            x = x * (-1)
            c = 1
        
        n = len(str(x))

        for i in range(n-1, -1, -1) : 
            last_int = x % 10
            res += (last_int * pow(10, i))
            x = x // 10

        if (lower <= res <= upper) :
            pass
        else :
            res = 0         
        if (c == 1) : 
            res = (res * (-1))
        else : 
            pass

        if (res == x_dup) :
            ans = True 
            
        return ans
            

        


a = Solution()
b = a.isPalindrome(121)
print(b)
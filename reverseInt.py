

# pseudocode:
# extract last int by taking mod 10 
# multiply last int by pow(10, len)
# add this to our final result 
# remove last digit by float division by 10 (x // 10)
# for loop should run len number of times 
# return result 


class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """

        
        res = 0
        c = 0

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
            return res         

        if (c == 1) : 
            return (res * (-1))
        else : 
            print("here")
            return res
            

        


a = Solution()
b = a.reverse(-123)
print(b)

'''

return n!

'''

def factorial(n):
    result = 1

    for i in range(1, n+1):
        result *= i

    return result 


n = 5
res = factorial(n)
print("Answer:", res)
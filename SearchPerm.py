# program to count number of permutations of string b 
# that are within string s 


def countPerm(b, s) :

    if len(b) == 0 or len(s) == 0:
        return 0

    start = 0
    count = 0
    b_len = len(b)
    s_len = len(s) + 1
    temp = ""

    while b_len != s_len :
        temp = s[start: b_len]
        if isPerm(b, temp) == True :
            count += 1

        start += 1
        b_len += 1

    return count



def isPerm(a, b) :
    # return true if strings a and b are 
    # permutations 
    if len(a) != len(b) :
        return False

    result = True

    for i in a:
        if i not in b:
            result = False
            return result 

    return result

    
            

# testing 
b = "abc"
s = "abcdefghab"


ans = countPerm(b, s)
print("answer:", ans)



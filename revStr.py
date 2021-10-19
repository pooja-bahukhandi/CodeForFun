# reverse a string in python

def Reverse(s):
    length = len(s)
    temp_len = length - 1
    new_s = ""

    if length == 0 :
        return new_s

    for i in range(0, length) :
        a = temp_len 

        new_s += s[a]

        temp_len -= 1

    return new_s


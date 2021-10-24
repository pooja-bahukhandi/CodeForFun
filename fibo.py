''' 

print first n terms of fibonacci sequence

ex1: n = 1 => 1
ex2: n = 2 => 1,1
ex3: n = 3 => 1,1,2


'''

def fibo(n) :
    a = 1
    b = 1

    print(a)
    print(b)

    if n > 2:
        count = 2
        while count < n:
            temp = a+b
            print(temp)
            count += 1
            temp2 = a
            a = b
            b = temp
            




n = 4
fibo(n)



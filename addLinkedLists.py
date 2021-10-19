# medium level 

# pseudocode: 
# modify l1 to include its powers of 10 
# add the powers of 10 from l2 into l1 
# return l1 


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        list_to_int(l1.reversed())


        return l1


# function to convert list to int 
# input : list(int)
# output : int 

def list_to_int(input_list):
    #l=[1,2,3]
    #output = 123 
    length_list = input_list.__len__()
    res = 0
    length_list -= 1
    x = 0


    for i in input_list : 
        x += i * pow(10,length_list)
        length_list -= 1

    return x


 





        





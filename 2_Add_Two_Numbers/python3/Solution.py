# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Solution.py                                        :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: inazaria <inazaria@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/06/16 02:18:16 by inazaria          #+#    #+#              #
#    Updated: 2024/06/22 20:13:39 by inazaria         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys
from typing import Optional

# didn't that know that you could do forward referencing in type hinting !

class ListNode:
    def __init__(self, val=0, next: Optional["ListNode"] = None):
        self.val: int = val
        self.next: Optional["ListNode"] = next

    def getNumber(self, head: Optional["ListNode"] = None) -> int :
        num: str = ""
        if head == None :
            return 0

        while head.next != None :
            num += str(head.val)
            head = head.next

        
        return int(num[::-1])

    def putNumber(self, number_rev_list: list[str]) -> None :
        
        if number_rev_list == [] :
            return None

        self.val= int(number_rev_list[0])
        tmp = ListNode(0, None)
        self.next = tmp
        return tmp.putNumber(number_rev_list[1:])

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        l3: ListNode = ListNode(0, None)
        tmp: ListNode = l3
        
        carry: int = 0
        sum: int = 0

        #print(f"sum : {sum} carry : {carry}")
        while l1 != None or l2 != None :
            x: int = l1.val if l1 != None else 0
            y: int = l2.val if l2 != None else 0
            
            sum: int = carry + x + y
            tmp.next = ListNode(sum % 10)            
            carry = 1 if (l1 != None or l2 != None) and sum > 9 else 0
            tmp = tmp.next

            if l1 != None : l1 = l1.next
            if l2 != None : l2 = l2.next
        
        if carry > 0 and sum > 9:
            tmp.next = ListNode(1)
            

        return l3.next




if __name__ == "__main__" :
    if (len(sys.argv) != 3) :
        print(f"Usage : python3 Solution.py <list1> <list2")
        print("Example : python Solution.py '[1,6,2]' '[1,4,5]' ")
        sys.exit(1)

    try :
        num1_rev_lst: list[str] = eval(sys.argv[1])

        num2_rev_lst: list[str] = eval(sys.argv[2])

    except Exception as e :
        print(f"Error : {e}")        
        print(f"\nUsage : python3 Solution.py <list1> <list2>")
        print("Example : python Solution.py '[1,6,2]' '[1,4,5]' ")
        sys.exit(1)

    num1: ListNode = ListNode(0, None)
    num1.putNumber(num1_rev_lst)

    num2: ListNode = ListNode(0, None)
    num2.putNumber(num2_rev_lst)

    answer: Optional[ListNode] = Solution().addTwoNumbers(num1, num2)

    print(f"num1 : {ListNode().getNumber(num1)} + num2 : {ListNode().getNumber(num2)} \
= {ListNode().getNumber(answer)}")
    








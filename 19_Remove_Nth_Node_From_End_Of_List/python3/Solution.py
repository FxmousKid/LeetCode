# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Solution.py                                        :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: inazaria <inazaria@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/06/22 20:02:51 by inazaria          #+#    #+#              #
#    Updated: 2024/06/22 20:55:47 by inazaria         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys
from typing import Optional

class ListNode:
    def __init__(self, val=0, next: Optional["ListNode"] = None):
        self.val: int = val
        self.next: Optional["ListNode"] = next

    def getNumber(self, head: Optional["ListNode"] = None) -> list[str] :
        num: list[str] = []
        if head == None :
            return []

        while head.next != None :
            num.append (str(head.val))
            head = head.next

        
        return num

    def putNumber(self, number_lst: list[str]) -> None :
        
        if number_lst == [] :
            return None

        self.val= int(number_lst[0])
        tmp = ListNode(0, None)
        self.next = tmp
        return tmp.putNumber(number_lst[1:])


class Solution:


    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        tmp1: Optional[ListNode] = head
        len_lst: int = 0

        while (tmp1 and tmp1.next) :
            if tmp1.next and tmp1.next.next == None and n == 1 :
                tmp1.next = None
                return head 

            len_lst += 1
            tmp1 = tmp1.next
       
        tmp2: Optional[ListNode] = head
        nth_node_idx: int = len_lst - n
 
        if n == len_lst :
            head = head.next if head else head
            return head

        # this is to get to the node before the one we want to remove
        while (tmp2 and nth_node_idx > 1) :
            tmp2 = tmp2.next
            nth_node_idx -= 1

        if (tmp2 and tmp2.next and tmp2.next.next == None) :
            tmp2.next = None

        elif tmp2 and tmp2.next :
            tmp2.next = tmp2.next.next

        return head
        




if __name__ == "__main__" :
    if (len(sys.argv) != 3) :
        print(f"Usage : python3 Solution.py <list1> <n>")
        print("Example : python Solution.py '[1,6,2]' '2' ")
        sys.exit(1)

    try :
        num1_lst: list[str] = eval(sys.argv[1])
        nth_node: int = int(sys.argv[2])

    except Exception as e :
        print(f"Error : {e}")        
        print(f"\nUsage : python3 Solution.py <list1> <n>")
        print("Example : python Solution.py '[1,6,2]' '2' ")
        sys.exit(1)

    num1: ListNode = ListNode(0, None)
    num1.putNumber(num1_lst)


    print(f"before removing node {nth_node} : {ListNode().getNumber(num1)}")
    answer = Solution().removeNthFromEnd(num1, nth_node)
    print(f"after  removing node {nth_node} : {ListNode().getNumber(answer)}")


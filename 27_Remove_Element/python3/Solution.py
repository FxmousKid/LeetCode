# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Solution.py                                        :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: inazaria <inazaria@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/06/12 22:08:01 by inazaria          #+#    #+#              #
#    Updated: 2024/06/12 23:14:14 by inazaria         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys
from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:        
        i : int = 0
        while (i < len(nums)) :
            if (nums[i] == val) :
                nums.pop(i)
            else :
                i += 1

        return (len(nums))


if __name__ == "__main__" :
    if (len(sys.argv) != 3) :
        print("Usage: python3 Solution.py <\"[1,2,3,...]\"> <val>")
        sys.exit(1)
    lst : list[int] = eval(sys.argv[1])
    print(f"list = {lst}, val = {sys.argv[2]}")
    res : int = Solution().removeElement(lst, int(sys.argv[2]))
    print(f"List = {lst}, result = {res}")
    sys.exit(0)

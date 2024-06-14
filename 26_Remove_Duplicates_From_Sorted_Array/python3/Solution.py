# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Solution.py                                        :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: inazaria <inazaria@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/06/12 18:45:04 by inazaria          #+#    #+#              #
#    Updated: 2024/06/12 22:07:20 by inazaria         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys
from typing import List

class Solution:    
    def removeDuplicates(self, nums: List[int]) -> int:
        i : int = 1
        len_nums : int = len(nums)

        while (i < len_nums) :
            while (nums[i - 1] == nums[i]) :
                nums.pop(i)
                if (i == len(nums)) :
                    break
            i += 1
            len_nums = len(nums)

        return (len(nums))

if __name__ == "__main__":
    if (len(sys.argv) != 2):
        print("Usage : python3 Solution.py <\"[1,2,3,4,...]\">")
        sys.exit(1) 

    lst = eval(sys.argv[1])
    print(f"Before removing dupes : {lst}")
    k : int = Solution().removeDuplicates(lst)
    print(f"After removing dupes  : {lst} with k = {k}",)
    sys.exit(0)


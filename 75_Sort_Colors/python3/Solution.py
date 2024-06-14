# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Solution.py                                        :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: inazaria <inazaria@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/06/12 14:15:37 by inazaria          #+#    #+#              #
#    Updated: 2024/06/12 17:24:27 by inazaria         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

class Solution:

    def getLastIndex(self, nums: list[int], n: int) -> int :
        index : int = 0
        for idx, val in enumerate(nums):
            if val == n :
                index = idx
        return index

    def isSorted(self, nums: list[int]) -> bool :
        if (len(nums) <= 1) :
            return True

        for idx, val in enumerate(nums[1:], start=0) :
            if (val < nums[idx]) :
                return False

        return True

    def sortColors(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if (len(nums) <= 1) :
            return 

        for idx, val in enumerate(nums) :
            if (not(self.isSorted(nums[:idx + 1]))) :
                if (val == 0) :
                    nums.insert(0, nums.pop(idx))
                if (val == 1 and 0 in nums[:idx + 1]) :
                    nums.insert(self.getLastIndex(nums[:idx], 0) + 1, nums.pop(idx))
                if (val == 1 and 0 not in nums[:idx + 1]) :
                    nums.insert(0, nums.pop(idx))

if __name__ == "__main__" :
    if (len(sys.argv) <= 1) :
        print("Usage: python3 Solution.py <num1> <num2> ... <numN>")
        print("with 0 <= num <= 2")
        sys.exit(1) 
    try :
        lst = list(map(int, sys.argv[1:]))
    except ValueError :
        print("Value has to be an int : 0 <= Value <= 2")
        sys.exit(1)
    for num in lst : 
        if num not in [0, 1, 2] :
            print("the numbers have to be >= 0 and <= 2")
            sys.exit(1)
    print(f"List before sort : {lst}")
    Solution().sortColors(lst)
    print(f"List after sort : {lst}")
    sys.exit(0)
